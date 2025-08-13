FACTORIAL = 1
e_value = 0
e_sum = 1
for number in range(1, 11):
	FACTORIAL *= number
	e_value = 1/FACTORIAL
	print(e_value)
	e_sum += e_value
print(e_sum)
	 

	
