import unittest
import function_snacks

class TestFunctionSnacks(unittest.TestCase):
	def test_that_the_divide_or_square_function_exists(self):
		function_snacks.divide_or_square(5)
	def test_that_the_divide_or_square_function_raises_validation_with_incorrect_value(self):
		self.assertRaises(ValueError, function_snacks.divide_or_square, "name")
	def test_that_the_divide_or_square_function_raises_validation_with_negative__value(self):
		self.assertRaises(ValueError, function_snacks.divide_or_square, "-1")
	def test_that_the_divide_or_square_function_returns_correct_result_for_if(self):
		result = function_snacks.divide_or_square(10)
		self.assertEqual(result, 3.16)
	def test_that_the_divide_or_square_function_returns_correct_result_for_else(self):
		result = function_snacks.divide_or_square(11)
		self.assertEqual(result, 1)


class TestFuctionSnacks1(unittest.TestCase):
	def test_that_the_future_investment_function_exists(self):
		function_snacks.future_investment(5, 3, 2)
	def test_that_the_future_investment_function_raises_validation_with_incomplete_arguement(self):
		self.assertRaises(ValueError, function_snacks.future_investment, 0, 0, 0)
	def test_that_the_future_investment_function_raises_validation_with_string_value(self):
		self.assertRaises(ValueError, function_snacks.future_investment, "name", "word", "phrase")
	def test_that_the_future_investment_function_raises_validation_with_negative_value(self):
		self.assertRaises(ValueError, function_snacks.future_investment, -1, -2, -3)
	def test_that_the_future_investment_converts_returns_correct_result_for_future_investment(self):
		result = function_snacks.future_investment(5, 3, 2)
		self.assertEqual(result, 1407374883553280)
	
class TestFunctionSnacks2(unittest.TestCase):
	def test_that_the_only_floats_function_exists(self):
		function_snacks.only_floats(5, 3)
		
	def test_that_the_only_floats_function_returns_the_corect_result_when_the_two_arguements_are_float(self):
		result = function_snacks.only_floats(0.5, 1.5)
		self.assertEqual(result, 2)
		
	def test_that_the_only_floats_function_returns_the_corect_result_when_the_one_arguement_is_float_and_the_other_not_float(self):
		result = function_snacks.only_floats(0.5, 5)
		self.assertEqual(result, 1)
		
	def test_that_the_only_floats_function_returns_the_corect_result_when_neither_of_the_arguement_is_float(self):
		result = function_snacks.only_floats(5, 5)
		self.assertEqual(result, 0)
		
	def test_that_the_only_floats_function_returns_validation_if_one_arguement_is_empty(self):
		self.assertRaises(ValueError, function_snacks.only_floats, "", 5.9)

	def test_that_the_only_floats_function_returns_validation_if_one_arguement_is_empty(self):
		self.assertRaises(ValueError, function_snacks.only_floats, -5.3, -6.7)

	
		


	

	



	
