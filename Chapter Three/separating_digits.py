#3.9(Separating the digits in an integer)
integer = int(input("Enter a five-digit integer: "))

for count in range(5):
	digit = integer % 10
	integer = integer // 10
	print(digit, end= ' ')
