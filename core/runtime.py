from datetime import datetime


class RuntimeManager:

    def __init__(self):

        self.start_time = None

        self.environment = None

        self.status = "STOPPED"


    def start(
            self,
            environment
    ):

        self.start_time = datetime.now()

        self.environment = environment

        self.status = "RUNNING"



    def stop(self):

        self.status = "STOPPED"



    def get_uptime(self):

        if not self.start_time:

            return "0s"


        delta = datetime.now() - self.start_time


        seconds = int(
            delta.total_seconds()
        )


        hours = seconds // 3600

        minutes = (
                          seconds % 3600
                  ) // 60

        seconds = seconds % 60


        return (
            f"{hours}h "
            f"{minutes}m "
            f"{seconds}s"
        )



    def get_status(self):

        return {

            "environment":
                self.environment,


            "status":
                self.status,


            "uptime":
                self.get_uptime()

        }