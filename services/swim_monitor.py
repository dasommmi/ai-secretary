import requests
from bs4 import BeautifulSoup

from models.course import Course


class SwimMonitor:

    URL = "https://spc2.y-sisul.or.kr/page/lect/lect.n.list.asp?page=1&s_key=vname&s_val=&s_lgu_seq=10&s_lcl_seq=109"

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "Mozilla/5.0"
        })

    def get_courses(self):

        response = self.session.get(
            self.URL,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.select("table.tbl_scm1 tbody tr")

        courses = []

        for row in rows:

            tds = row.select("td")

            if len(tds) < 8:
                continue

            course_name = tds[0].get_text(strip=True)

            remain = tds[7].get_text(strip=True)

            current, total = remain.split("/")

            status = tds[8].get_text(strip=True)

            courses.append(
                Course(
                    name=course_name,
                    remain=int(current),
                    total=int(total),
                    status=status
                )
            )

        return courses
