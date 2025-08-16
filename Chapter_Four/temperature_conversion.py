def convert_to_celsius_of(celsuis_value):
	return (9 / 5) * celsuis_value + 32
	

print("Number \t Fahrenheit_equivalent")
for number in range(0, 100):
	print(number, "\t", round(convert_to_celsius_of(number), 1))


