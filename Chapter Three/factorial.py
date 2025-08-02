#3.13  (Factorials) 
integer = 10
factorial_of_ten = 1
for number in range(10, 0, -1):
	factorial_of_ten *= number
print(factorial_of_ten)