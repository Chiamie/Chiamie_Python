import unittest
import inspect
import map_function_snack



class TestGetSquaresFunction(unittest.TestCase):
	def test_that_square_of_function_accepts_1_argument(self):
		function_signature = inspect.signature(map_function_snack.square)
		dic_parameter = function_signature.parameters
		self.assertEqual(len(dic_parameter), 1)
	def test_that_square_of_function_input_is_a_list(self):
		list_of_integers = [9, 6, 7]
		result = map_function_snack.square(list_of_integers)
		self.assertIsInstance(list_of_integers, list)
	def test_that_square_of_function_raises_validation_if_input_is_not_list(self):
		self.assertRaises(TypeError, map_function_snack.square, "name")
	def test_that_square_of_function_raises_validation_if_input_is_not_a_list_of_integers(self):
		list_of_integers = ['name', 'ayo', 'awele']
		self.assertRaises(ValueError, map_function_snack.square, list_of_integers)
	def test_that_square_of_function_returns_correct_result(self):
		result = map_function_snack.square([1, 2, 3, 4])
		self.assertEqual(result, [1, 4, 9, 16])

