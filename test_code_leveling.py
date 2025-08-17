import unittest
import code_leveling



class TestGetTheTotalOfFunction(unittest.TestCase):
	def test_that_get_the_total_of_function_receives_a_list_of_list_as_input(self):
		list_of_numbers = [[1, 5, 2], [3, 7, 4], [5, 8, 6]]
		result = code_leveling.get_the_total_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_the_total_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_the_total_of, "not a list")
	def test_that_the_get_the_total_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = [['name', 'amaka', 'ayo'], ['awele', 'nutrient', 'plate']]
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_raises_validation_if_a_list_contains_non_numeric(self):
		list_of_integers = [[1, 5, 2], [3, 7, 4], [5, 'a', 6]]
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_raises_validation_if_a_sublist_has_negative_number(self):
		list_of_integers = [[1, 5, -2], [3, 7, 4], [5, 8, 6]]
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_returns_correct_result(self):
		result = code_leveling.get_the_total_of([[1, 5, 2], [3, 7, 4], [5, 8, 6]])
		self.assertEqual(result, [8, 14, 19])



class TestGetSumOfFunction(unittest.TestCase):
	def test_that_the_get_sum_of_function_receives_a_list_of_list_as_input(self):
		list_of_numbers = [[1, 5, 2], [3, 7, 4], [5, 8, 6]]
		result = code_leveling.get_sum_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_sum_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_sum_of, "not a list")
	def test_that_the_get_sum_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = [['name', 'amaka', 'ayo'], ['awele', 'nutrient', 'plate']]
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_raises_validation_if_a_list_contains_non_numeric(self):
		list_of_integers = [[1, 5, 2], [3, 7, 4], [5, 'a', 6]]
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_raises_validation_if_a_sublist_has_negative_number(self):
		list_of_integers = [[1, 5, -2], [3, 7, 4], [5, 8, 6]]
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_returns_correct_result(self):
		result = code_leveling.get_sum_of([[1, 5, 2], [3, 7, 4], [5, 8, 6]])
		self.assertEqual(result, [9, 20, 12])




	

		 