class Message:
    def __init__(self):
        self.inbox = {}

    def is_empty(self):
        return self.inbox == {}