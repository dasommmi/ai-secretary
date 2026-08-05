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

        self.playwright: Playwright | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    def start(self):

        self.user_data_dir.mkdir(parents=True, exist_ok=True)

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=str(self.user_data_dir),
            headless=self.headless,
        )

        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

    def close(self):

        if self.context:
            self.context.close()

        if self.playwright:
            self.playwright.stop()
