from domain.knowledge.category import get_category_name


class DailyDigestScheduler:

    def __init__(self, use_case, notifier):

        self.use_case = use_case

        self.notifier = notifier

        from apscheduler.schedulers.background import BackgroundScheduler

        self.scheduler = BackgroundScheduler()

    def start(self):

        print("🔥 DailyDigestScheduler started")

        self.scheduler.add_job(
            self.execute,
            trigger="cron",
            hour=8,
            minute=30,
            max_instances=1,
            coalesce=True,
        )

        self.scheduler.start()

    def execute(self):

        print("🔥 Digest execute start")

        digest = self.use_case.execute()

        if digest is None:

            print("오늘 Digest 이미 존재")

            return

        print(f"생성된 Knowledge : {len(digest.items)}")

        for item in digest.items:

            category_name = get_category_name(item.category)

            message = f"""
🧠 오늘의 Knowledge Digest

{category_name}

Q. {item.question}

A. {item.answer}
""".strip()

            print(f"Telegram 전송 : {item.category}")

            self.notifier.send(message)

            # Telegram 연속 발송 방지

            # time.sleep(1)
