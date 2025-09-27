
class Phonebook:
    def __init__(self):
        self.contacts_book = {}

    def is_empty(self):
        return self.contacts_book == {}

    def add_contact(self, contact):
        self.contacts_book[contact[0]] = contact[1]


    def edit_contact(self, name, new_contact):
        if not name.isalpha():
            raise ValueError('Name must be an apha!')
        if not new_contact.isdigit():
            raise ValueError('New contact must be an integer!')
        for contact in self.contacts_book:
            if contact == name and new_contact.isdigit():
                self.contacts_book[name] = new_contact
            elif contact == name and new_contact.isalpha():
                self.contacts_book[new_contact] = self.contacts_book[name].pop(name)


    def search(self, name):
        return self.contacts_book.get(name)

    def get_contact(self):
        return self.contacts_book

    def erase(self):