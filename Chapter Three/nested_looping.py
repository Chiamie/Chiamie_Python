#3.18(Challenge: Nested Looping)

count = 0
number_rows = 10
for number in range(1, number_rows + 1):
	for digits in range(number):
		print("*", end= "")
	print(" " *(number_rows - number + 3), end= "")
	for digits in range(number_rows - number + 1):
		print("*", end= "")
	print(" " *(number_rows + number - 3), end= "")
	print(' '*(count + number), end= "")
	for digits in range(number_rows - number + 1):
		print("*", end= "")
	print(" " * 3, end= "")
	print(' '*(count + number), end= "")
	for digits in range(number):
		print("*",end=" ")
	print()

	
	
	