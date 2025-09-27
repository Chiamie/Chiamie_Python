import unittest

from Nokia.PhoneBook import Phonebook


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = Phonebook()

    def test_that_phonebook_is_empty(self):
        self.assertTrue(self.phone_book.is_empty(), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
