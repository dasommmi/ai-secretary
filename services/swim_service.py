from bot.sender import send_message
from core.base_service import BaseService
from services.swim_monitor import SwimMonitor


class SwimService(BaseService):

    TARGETS = [
        "[2026추첨]저녁수영20B(여성)(평영 이상 등록가능)"
    ]

    def __init__(self):

        self.monitor = SwimMonitor()

        self.last = {}

    def check(self):

        courses = self.monitor.get_courses()

        for course in courses:

            if course.name not in self.TARGETS:
                continue

            print(
                f"{course.name} : {course.remain}/{course.total}"
            )

            previous = self.last.get(
                course.name,
                -1
            )

            if (
                    course.remain > 0
                    and previous != course.remain
            ):

                send_message(
                    f"""
🏊 자리 발생!

강좌

{course.name}

현재

{course.remain}/{course.total}

{self.monitor.URL}
"""
                )

            self.last[
                course.name
            ] = course.remain