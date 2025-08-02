import unittest
import dollar_to_naira
class TestDollarToNairaFunction(unittest.TestCase):
	def test_that_dollar_to_naira_function_exists(self):
		dollar_to_naira.get_dollar_amount(500)
	
	def test_that_dollar_to_naira_function_returns_correct_equivalence(self):
		equivalence = dollar_to_naira.get_dollar_amount(500)
		self.assertEqual(equivalence, 775000)
		
	def test_that_dollar_to_naira_function_raises_error_with_incorrect_value(self):
		self.assertRaises(ValueError, dollar_to_naira.get_dollar_amount, "money")

	def test_that_dollar_to_naira_function_returns_correct_approximated_figure(self):
		equivalence = dollar_to_naira.get_dollar_amount(419.12)
		self.assertEqual(equivalence, 649_636)

	
		
	