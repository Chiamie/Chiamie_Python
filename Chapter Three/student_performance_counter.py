#3.1(Validating User Input)
passes = 0
failures = 0

for student in range(10):
	result = int(input("Enter result (1 = pass, 2 = fail): "))
	while True:
		if result == 1:
			passes = passes + 1
			break
		elif result == 2:
			failures = failures + 1
			break
		else:
			result = int(input("Enter result (1 = pass, 2 = fail): "))
		
print("Passed:", passes)
print("failed:", failures)

if passes > 8:
	print("Bonus to instructor")

