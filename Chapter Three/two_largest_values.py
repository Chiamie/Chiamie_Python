#3.16(Nested Control Statements
largest = 0
second_largest = largest
for counts in range(10):
	number = int(input("Enter an intger: "))
	if number > largest:
		second_largest = largest
		largest = number
	if number > second_largest and largest != number:
			second_largest = number
print(largest)
print(second_largest)
