from apscheduler.schedulers.background import BackgroundScheduler


class DailyDigestScheduler:

    def __init__(self, use_case, notifier):

        self.use_case = use_case

        self.notifier = notifier

        self.scheduler = BackgroundScheduler(timezone="Asia/Seoul")

    def start(self):

        self.scheduler.add_job(self.execute, trigger="cron", hour=8, minute=30)

        self.scheduler.start()

    def execute(self):

        try:

            digest = self.use_case.execute()

            if digest is None:

                return

            message = self._format_message(digest)

            self.notifier.send(message)

        except Exception as e:

            print("Digest Scheduler Error", e)

    def _format_message(self, digest):

        result = []

        result.append("🧠 오늘의 Knowledge Digest\n")

        for item in digest.items:

            result.append(f"""
[{item.category}]

Q. {item.question}

A. {item.answer}

""")

        return "\n".join(result)
