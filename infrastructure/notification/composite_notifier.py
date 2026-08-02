class CompositeNotifier:

    def __init__(self, notifiers):

        self.notifiers = notifiers

    def send(self, message: str):

        for notifier in self.notifiers:

            notifier.send(message)
