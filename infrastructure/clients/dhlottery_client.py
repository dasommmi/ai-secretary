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

    def login(self):

        self.browser.start()

        page = self.browser.page

        page.goto(self.LOGIN_URL)

        page.get_by_role("textbox", name="아이디").fill(LOTTO_ID)

        page.get_by_role("textbox", name="비밀번호").fill(LOTTO_PASSWORD)

        page.locator("#btnLogin").click()

        try:
            page.get_by_role(
                "button",
                name="오늘 그만 보기",
            ).click(timeout=3000)

        except Exception:
            pass

    def close(self):

        self.browser.close()
