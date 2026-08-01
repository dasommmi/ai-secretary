from apscheduler.schedulers.background import BackgroundScheduler


class DailyDigestScheduler:

    def __init__(self, use_case):

        self.use_case = use_case

        self.scheduler = BackgroundScheduler(timezone="Asia/Seoul")

    def start(self):

        self.scheduler.add_job(self.execute, trigger="cron", hour=8, minute=30)

        self.scheduler.start()

    def execute(self):

        try:

            digest = self.use_case.execute()

            if digest is None:

                print("오늘 Digest는 이미 생성됨")

                return

            print("Daily Digest 생성 완료", digest)

        except Exception as e:

            print("Daily Digest 생성 실패", e)
