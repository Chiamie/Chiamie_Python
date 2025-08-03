import unittest
import inspect
from celsius_to_fahrenheit_converter import celsius_to_fahrenheit
class TestCelsiusToFahrenheitFunction(unittest.TestCase):
	def test_that_celsius_to_fahrenheit_function_accepts_inputs(self):
		function_signature = inspect.signature(celsius_to_fahrenheit)
		dic_parameter = function_signature.parameters
		self.assertEqual(len(dic_parameter), 2)
	def test_that_the_celsius_to_fahrenheit_function_raises_validation_with_incorrect_value_for_first_parameter(self):
		self.assertRaises(TypeError, celsius_to_fahrenheit("string", "string"))
	def test_that_the_celsius_to_fahrenheit_function_raises_validation_with_incorrect_value_for_second_parameter(self):
		self.assertRaises(TypeError, celsius_to_fahrenheit(30, 30))
	def test_that_the_celsius_to_fahrenheit_function_raises_validation_with_incorrect_value_for_the_two_parameters(self):
		self.assertRaises(TypeError, celsius_to_fahrenheit(32.8, 32.8))
	def test_that_the_celsius_to_fahrenheit_function_raises_validation_with_incorrect_value_for_second_parameter(self):
		self.assertRaises(TypeError, celsius_to_fahrenheit("string", 32.8))
	def test_that_the_celsius_to_fahrenheit_function_raises_validation_with_incorrect_value_for_the_two_parameter(self):
		self.assertRaises(TypeError, celsius_to_fahrenheit("string", 45))
	def test_that_the_celsius_to_fahrenheit_function_raises_validation__when_first_parameter_is above_absolute_zero_in_celsius(self):
		self.assertRaises(ValueError, celsius_to_fahrenheit(-300, 'c'))
	def test_that_the_celsius_to_fahrenheit_function_raises_validation__when_first_parameter_is above_absolute_zero_in_fahrenheit(self):
		self.assertRaises(ValueError, celsius_to_fahrenheit(500, 'f'))


		



		