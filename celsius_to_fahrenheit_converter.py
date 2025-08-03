def celsius_to_fahrenheit(temperature, unit):
	if not isinstance(temperature, (int, float)) or not isinstance(unit, (str)):
		raise TypeError("Temperature value must be a number while second must be a string")
	if unit.lower != 'C' or unit.lower != 'F':
		raise ValueError("Unit value must either be 'C' or 'F'")
	if unit.lower == 'C' and temperature < -273.15:
		raise ValueError("Temperature cannot be below absolute zero")


