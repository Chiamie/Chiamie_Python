#3.17(Nested Loops)
for number in range(1, 11):
	for digits in range(number):
		print("*", end= "")
	print()
print()

for number in range(10, 0, -1):
	for digits in range(number):
		print("*", end= "")
	print()
print()		

count = 0
for number in range(10, 0, -1):
	print(' '*count, end= "")
	for digits in range(number):
		print("*", end= "")
	print()
	count += 1
print()		

count = 9
for number in range(1, 11):
	print(' '*count, end= "")
	for digits in range(number):
		print("*", end= "")
	print()
	count -= 1
print()
