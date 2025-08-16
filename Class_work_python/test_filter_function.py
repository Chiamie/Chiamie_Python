import unittest
import inspect
import filter_function



class TestGetIsEvenOfFunction(unittest.TestCase):
	def test_that_get_is_even_of_function_accepts_1_argument(self):
		function_signature = inspect.signature(filter_function.get_is_even_of)
		dic_parameter = function_signature.parameters
		self.assertEqual(len(dic_parameter), 1)
	def test_that_get_is_even_of_function_input_is_a_list(self):
		list_of_integers = [9, 6, 7]
		result = filter_function.get_is_even_of(list_of_integers)
		self.assertIsInstance(list_of_integers, list)
	def test_that_get_is_even_of_function_raises_validation_if_input_is_not_list(self):
		self.assertRaises(TypeError, filter_function.get_is_even_of, "name")
	def test_that_get_is_even_of_function_raises_validation_if_input_is_not_a_list_of_integers(self):
		list_of_integers = ['name', 'ayo', 'awele']
		self.assertRaises(ValueError, filter_function.get_is_even_of, list_of_integers)
	def test_that_get_is_even_of_function_returns_correct_result(self):
		result = filter_function.get_is_even_of([1, 2, 3, 4, 5, 6])
		self.assertEqual(result, [2, 4, 6])



