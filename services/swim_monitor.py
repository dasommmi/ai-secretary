import re

import requests
from bs4 import BeautifulSoup


class SwimMonitor:

    URL = "https://spc2.y-sisul.or.kr/page/lect/lect.n.list.asp?page=1&s_key=vname&s_val=&s_lgu_seq=10&s_lcl_seq=109"

    TARGET = "[2026추첨]저녁수영20B(여성)(평영 이상 등록가능)"

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache"
        })

    def check(self):

        response = self.session.get(
            self.URL,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        rows = soup.select("table.tbl_scm1 tbody tr")

        for row in rows:

            text = row.get_text(" ", strip=True)

            if self.TARGET not in text:
                continue

            match = re.search(r"(\d+)\s*/\s*(\d+)", text)

            if not match:
                raise Exception("좌석 정보를 찾을 수 없습니다.")

            remain = int(match.group(1))
            total = int(match.group(2))

            return remain, total

        raise Exception("강좌를 찾을 수 없습니다.")