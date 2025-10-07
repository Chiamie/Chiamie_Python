import unittest
from Account_file import Account


class TestSetNameFunction(unittest.TestCase):
    def setUp(self):
        self.account1 = Account('Ada', "5chiamie234","06-07-1967", 100)

    def test_that_an_account_number_was_generated_for_Ada(self):
        self.assertEqual(self.account1.account_number, "5chiamie234")

    def test_that_set_name_raises_exception_when_name_is_numeric_string(self):
        self.assertRaises(ValueError, self.account1.set_name, '1234')

    def test_that_set_name_raises_exception_when_name_is_not_string(self):
        self.assertRaises(ValueError, self.account1.set_name, ["Jay", "Yeh"])

    def test_that_set_name_raises_exception_when_name_is_not_alpha_string(self):
        self.assertRaises(ValueError, self.account1.set_name, "@ghu76.,")

    def test_that_account_validates_the_value_of_name_before_initializing(self):
        self.assertEqual(self.account1.name, 'Ada')

    def test_that_account_validates_the_value_of_name_before_assigning(self):
        self.account1.set_name('Nneka')
        self.assertEqual(self.account1.name, 'Nneka')



    def test_that_deposit_function_accepts_only_numeric_character(self):
        self.assertRaises(ValueError, self.account1.deposit, "chiamie")
    def test_that_amount_is_validated_before_intializing_to_balance(self):
        self.assertEqual(self.account1.balance, 100)

    def test_that_balance_increments_correctly_after_deposit(self):
        self.account1.deposit(200)
        self.assertEqual(self.account1.get_balance(), 300)

    def test_that_an_exception_is_raised_when_amount_to_be_deposited_is_less_than_0(self):
        self.assertRaises(ValueError, self.account1.deposit, -60)

    def test_that_an_exception_is_raised_when_amount_to_be_deposited_is_equal_to_0(self):
        self.assertRaises(ValueError, self.account1.deposit, 0)

    def test_that_an_exception_is_raised_when_amount_to_be_deposited_is_float(self):
        self.assertRaises(ValueError, self.account1.deposit, 15.4)

    def test_that_password_is_validated_before_withdrawal_is_made(self):
        password = "5chiamie234"
        self.account1.withdraw(100, password)
        self.assertEqual(self.account1.get_balance(), 0)

    def test_that_a_validation_is_raised_when_password_is_invalid(self):
        password = "5Chiamie234"
        self.assertRaises(ValueError, self.account1.withdraw, 20, password)

    def test_that_balance_decrements_correctly_when_amount_to_withdraw_is_integer(self):
        password = "5chiamie234"
        self.account1.withdraw(50, password)
        self.assertEqual(self.account1.get_balance(), 50)

    def test_that_balance_decrements_correctly_when_amount_to_withdraw_is_decimal(self):
        self.account1.withdraw(50.7, "5chiamie234")
        self.assertEqual(self.account1.get_balance(), 49.3)

    def test_that_an_exception_is_raised_when_amount_to_withdraw_is_greater_than_balance(self):
        self.assertRaises(ValueError, self.account1.withdraw, 200, "5chiamie234")

    def test_that_an_exception_is_raised_when_amount_to_withdraw_is_less_than_0(self):
        self.assertRaises(ValueError, self.account1.withdraw, -18, "5chiamie234")

    def test_that_an_exception_is_raised_when_date_has_incorrect_format(self):
        self.assertRaises(ValueError, self.account1.set_date, "1997-13-35")

    def test_that_an_exception_is_raised_when_date_is_not_a_string(self):
        self.assertRaises(ValueError, self.account1.set_date, 19975)

    def test_that_date_is_validated_before_assigning_to_date_of_birth(self):
        self.account1.set_date("11-03-1912")
        self.assertEqual(self.account1.get_date(), "11-03-1912")

    #def test_that_an_exception_is_raised_when_






