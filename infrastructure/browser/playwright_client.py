from pathlib import Path

from playwright.sync_api import (
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)


class PlaywrightClient:

    def __init__(
        self,
        headless: bool = True,
        user_data_dir: str = "infrastructure/browser/user_data",
    ):

        self.headless = headless
        self.user_data_dir = Path(user_data_dir)

        self._playwright: Playwright | None = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None

    def start(self) -> Page:

        self.user_data_dir.mkdir(parents=True, exist_ok=True)

        self._playwright = sync_playwright().start()

        self._context = self._playwright.chromium.launch_persistent_context(
            user_data_dir=str(self.user_data_dir),
            headless=self.headless,
        )

        pages = self._context.pages

        if pages:

            self._page = pages[0]

        else:

            self._page = self._context.new_page()

        return self._page

    def close(self):

        if self._context:

            self._context.close()

        if self._playwright:

            self._playwright.stop()
