class Tone:
    pass


class Phonebook:
    def __init__(self):
        self.contacts_book = {}
        self.name = ""
        self.number = ""
        self.tone = Tone()

    def is_empty(self):
        return True

    def search(self, name):
        return self.contacts_book[name]

