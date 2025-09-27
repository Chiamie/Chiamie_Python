import unittest

from Nokia.PhoneBook import Phonebook


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = Phonebook()

    def test_that_contacts_book_is_empty(self):
        self.assertTrue(self.phone_book.is_empty(), True)

    def test_that_contacts_book_is_not_empty_when_item_is_added_to_it(self):
        contact = ["chiamaka", "08101235568"]
        self.phone_book.add_contact(contact)
        self.assertFalse(self.phone_book.is_empty(), False)# add assertion here

    def test_that_contact_can_be_added_and_gotten_back(self):
        contact = ["chiamaka", "08101235568"]
        self.phone_book.add_contact(contact)

        #result = self.phone_book.search("chiamaka")
        self.assertEqual(self.phone_book.get_contact(), {"chiamaka": "08101235568"})

    def test_that_contacts_book_values_can_be_edited(self):
        contact = ["chiamaka", "08101235568"]
        self.phone_book.add_contact(contact)

        self.phone_book.edit_contact("chiamaka", "08101111111")
        self.assertEqual(self.phone_book.search("chiamaka"),  "08101111111")


    def test_that_a_contact_can_be_deleted(self):
        contact = ["chiamaka", "08101235568"]
        self.phone_book.add_contact(contact)

        self.phone_book.erase("chiamaka")
        self.assertTrue(self.phone_book.is_empty(), True)

    def test that
if __name__ == '__main__':
    unittest.main()
