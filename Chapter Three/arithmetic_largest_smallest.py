integer1 = int(input("Enter the first Integer"))
count = 1
sum = 0
average = 0
product = 1
largest = 0
smallest = integer1
while count < 4:
	integer1 = int(input("Enter the first Integer"))
	if integer1 > largest:
		largest = integer1
	if integer1 < smallest:
		smallest = integer1
	sum += integer1
	average = sum / (count + 1)
	product *= integer1
	count += 1
print(sum)
print(average)
print(product)
print(largest)
print(smallest)

