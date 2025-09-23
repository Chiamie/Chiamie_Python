import unittest
import boolean_perfect_square
import inspect



class TestGetSquaresFunction(unittest.TestCase):
	def test_that_get_square_of_function_accepts_1_argument(self):
		function_signature = inspect.signature(boolean_perfect_square.get_perfect_square)
		dic_parameter = function_signature.parameters
		self.assertEqual(len(dic_parameter), 1)
		
	def test_that_get_square_of_function_input_is_a_list(self):
		list_of_integers = [9, 6, 7]
		result = boolean_perfect_square.get_perfect_square(list_of_integers)
		self.assertIsInstance(list_of_integers, list)
		
	def test_that_get_square_of_function_raises_validation_if_input_is_not_list(self):
		self.assertRaises(TypeError, boolean_perfect_square.get_perfect_square, "name")
		
	def test_that_get_square_of_function_raises_validation_if_input_is_not_a_list_of_integers(self):
		list_of_integers = ['name', 'ayo', 'awele']
		self.assertRaises(ValueError, boolean_perfect_square.get_perfect_square, list_of_integers)
		
	def test_that_get_square_of_function_returns_correct_result(self):
		result = boolean_perfect_square.get_perfect_square([2, 3, 4])
		self.assertEqual(result, [False, False, True])
