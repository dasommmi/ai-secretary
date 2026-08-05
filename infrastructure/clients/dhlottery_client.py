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

        self.page = None

    def start(self):

        self.browser.start()

        self.page = self.browser.page

        self._login_if_needed()

    def close(self):

        self.browser.close()

    def _login_if_needed(self):

        self.page.goto(self.LOGIN_URL)

        # 이미 로그인 상태인지 확인
        if self._is_logged_in():

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

        try:

            self.page.get_by_role(
                "button",
                name="오늘 그만 보기",
            ).click(timeout=3000)

        except Exception:

            pass

    def _is_logged_in(self):

        try:

            self.page.get_by_text(
                "로그아웃",
            ).wait_for(timeout=3000)

            return True

        except Exception:

            return False
