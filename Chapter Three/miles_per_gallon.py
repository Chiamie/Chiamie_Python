number_gallon = float(input("Enter the gallons used (-1 to end): "))
miles = int(input("Enter the miles driven: "))
miles_per_gallon = miles / number_gallon
print(miles_per_gallon)
total_miles_per_gallon = miles_per_gallon
count_miles_per_gallon = 0
sentinel_value = -1
while True:
	count_miles_per_gallon += 1
	number_gallon = float(input("Enter the gallons used (-1 to end): "))
	if number_gallon == sentinel_value:
		break
	miles = int(input("Enter the miles driven: "))
	miles_per_gallon = miles / number_gallon
	print(miles_per_gallon)
	total_miles_per_gallon += miles_per_gallon
average_miles_per_gallon = total_miles_per_gallon / count_miles_per_gallon
print(average_miles_per_gallon)




number_gallon = float(input("Enter the gallons used (-1 to end): "))
#miles = int(input("Enter the miles driven: "))
#miles_per_gallon = miles / number_gallon
#print(miles_per_gallon)
total_miles_per_gallon = 0
count_miles_per_gallon = 0
#sentinel_value = -1
while number_gallon != -1:
	count_miles_per_gallon += 1
	miles = int(input("Enter the miles driven: "))
	miles_per_gallon = miles / number_gallon
	print(miles_per_gallon)
	total_miles_per_gallon += miles_per_gallon
	number_gallon = float(input("Enter the gallons used (-1 to end): "))

average_miles_per_gallon = total_miles_per_gallon / count_miles_per_gallon
print("this is the average",average_miles_per_gallon)


