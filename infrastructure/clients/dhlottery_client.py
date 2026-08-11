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

    def purchase_lotto(self):

        if self.page is None:

            raise Exception("Client is not started")

        popup = self.open_lotto_popup()

        frame = popup.locator('iframe[name="ifrm_tab"]').content_frame

        print("lotto purchase page loaded")

        # 1. 자동선택
        frame.get_by_text(
            "자동선택",
            exact=True,
        ).click()

        print("auto select clicked")

        # 2. 적용수량 5게임
        frame.get_by_label(
            "적용수량",
        ).select_option("5")

        print("quantity selected: 5")

        # 3. 적용수량 확인
        frame.locator("#btnSelectNum").click()

        print("number selection confirmed")

        # 4. 구매하기
        frame.locator("#btnBuy").click()

        print("buy button clicked")

        # 5. 최종 구매 확인
        frame.locator("#popupLayerConfirm").get_by_role(
            "button",
            name="확인",
        ).click()

        print("purchase confirmed")

        # 6. 구매 완료/안내 팝업 확인
        frame.locator("#closeLayer").click()

        print("purchase result popup closed")

        popup.close()

        return True

    def purchase_pension_lottery(self):

        if self.page is None:
            raise Exception("Client is not started")

        print("opening pension lottery popup")

        with self.page.expect_popup() as popup_info:

            self.page.get_by_role(
                "button",
                name="연금복권720+",
            ).click()

        popup = popup_info.value

        popup.wait_for_load_state(
            "domcontentloaded",
            timeout=60000,
        )

        frame = popup.locator('iframe[name="ifrm_tab"]').content_frame

        print("pension lottery page loaded")

        # 1. 자동 번호
        frame.get_by_role(
            "link",
            name="자동 번호",
        ).click()

        print("pension auto number selected")

        # 2. 선택 완료
        frame.get_by_role(
            "link",
            name="선택 완료",
        ).click()

        print("pension number selection completed")

        # 3. 이미 판매된 번호인지 확인
        sold_out_message = frame.get_by_text(
            "선택하신 번호는 이미 판매가 완료되었습니다.",
            exact=True,
        )

        if sold_out_message.is_visible():

            print("selected number already sold")

            # 추천 번호 중 첫 번째 선택
            recommended_number = frame.locator('input[name="recomandCheckNum"]').first

            recommended_number.check()

            print("recommended number selected")

            # 추천 번호 선택
            frame.locator('a[onclick="recomandNumberSelect()"]').click()

            print("recommended number confirmed")

        # 4. 구매하기
        frame.get_by_role(
            "link",
            name="구매하기",
        ).click()

        print("pension buy button clicked")

        # 5. 구매 확인 팝업의 최종 구매하기
        frame.locator("#lotto720_popup_confirm").get_by_role(
            "link",
            name="구매하기",
        ).click()

        print("pension final purchase clicked")

        # 6. 구매 완료 여부 확인
        purchase_complete_message = frame.locator(
            "span.lotto720_popup_content_str.saleRetMsg"
        )

        purchase_complete_message.wait_for(
            state="visible",
            timeout=10000,
        )

        message = purchase_complete_message.inner_text().strip()

        if message == "구매가 완료되었습니다.":

            print("pension lottery purchase completed")

            return True

        print(
            "pension lottery purchase failed:",
            message,
        )

        return False
