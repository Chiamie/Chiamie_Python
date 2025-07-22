#Morning Snacks

a = 62
b = 89
c = 85
if a > b and a > c:
	largest = a
elif b > a and b > c:
	largest = b
elif c > a and c > b:
	largest = c
print(largest)


x = 42
y = 12
z = 55
if x > y and x > z:
	largest = x
elif y > x and y > z:
	largest = y
elif z > y and z > x:
	largest = z


if x < y and x < z:
	smallest = x
elif y < x and y < z:
	smallest = y
elif z < y and z < x:
	smallest = z


if smallest != x and  x != largest:
	second_largest = x
if y != smallest and  y != largest:
	second_largest = y
if z != smallest and  z != largest:
	second_largest = z
print(second_largest)
	
	
days = int(input("Which of the days do you want? "))
match days:
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")
	case 7:
		print("Sunday")
	
		
		

