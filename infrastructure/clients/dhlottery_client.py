from playwright.sync_api import Page

from config.settings import (
    LOTTO_HEADLESS,
    LOTTO_ID,
    LOTTO_PASSWORD,
)
from infrastructure.browser.playwright_client import PlaywrightClient


class DHLotteryClient:

    LOGIN_URL = "https://www.dhlottery.co.kr/login"

    def __init__(self):

        self.browser = PlaywrightClient(
            headless=LOTTO_HEADLESS,
        )

        self.page: Page | None = None

    def start(self):

        self.browser.start()

        self.page = self.browser.page

        self._login_if_needed()

    def close(self):

        self.browser.close()

    def _login_if_needed(self):

        print("login page loaded")

        self.page.goto(
            self.LOGIN_URL,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        if self._is_logged_in():

            print("already logged in")

            return

        self.page.get_by_role(
            "textbox",
            name="아이디",
        ).fill(LOTTO_ID)

        self.page.get_by_role(
            "textbox",
            name="비밀번호",
        ).fill(LOTTO_PASSWORD)

        self.page.locator("#btnLogin").click()

        self.page.wait_for_timeout(3000)

        self._close_login_popup()

        print(
            "login finished:",
            self.page.url,
        )

    def _close_login_popup(self):

        try:

            self.page.get_by_role(
                "button",
                name="오늘 그만 보기",
            ).click(timeout=3000)

            print("popup closed")

        except Exception:

            print("no popup")

    def _is_logged_in(self):

        try:

            self.page.get_by_text("로그아웃").wait_for(timeout=10000)

            return True

        except Exception:

            return False

    def open_lotto_popup(self):

        if self.page is None:

            raise Exception("Client is not started")

        print("opening lotto popup")

        with self.page.expect_popup() as popup_info:

            self.page.get_by_role(
                "button",
                name="로또6/",
            ).click()

        popup = popup_info.value

        popup.wait_for_load_state(
            "domcontentloaded",
            timeout=60000,
        )

        print(
            "lotto popup:",
            popup.url,
        )

        return popup
