number = int(input("Enter a number: "))
if number < 10000 or number > 99999:
	print("Invalid input")
else:
	digit1 = number // 10000
	digit2 = (number // 1000) % 10
	digit3 = (number // 100) % 10
	digit4 = (number // 10) % 10
	digit5 = number % 10
	if digit1 == digit5 and digit2 == digit4:
		print("Number is a palindrome")
	else:
		print("Not a palindrome")
		