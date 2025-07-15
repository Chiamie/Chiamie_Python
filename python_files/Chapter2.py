#Dietel Python Text: Chapter Two
#Exercise 2.5 
radius = 2
pi = 3.14159 
diameter = 2 * radius
area = pi * radius * 2
circumference = 2 * pi * radius
print('The diameter of the circle is', diameter,', and the area is', area, ' while the circumference is', circumference)


#Exercise 2.6
number = 85
if number % 2 == 0:
    print(number, " is an even number.")

if number % 2 != 0:
    print(number, " is an odd number.")


#Exercise 2.7
number = 1024
number1 = 2
if number % 4 != 0:
    print(number, " is not a multiple of 4.")
if number % 4 == 0:
    print(number, " is a multiple of 4.")
if number1 % 10 != 0:
    print(number1, " is not a multiple of 10.")
if number1 % 10 == 0:
    print(number1, " is a multiple of 10.")


#Exercise 2.8(Table of Squares and Cubes)
number = 0
number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
square = number * number
square1 = number1 * number1
square2 = number2 * number2
square3 = number3 * number3
square4 = number4 * number4
square5 = number5 * number5

cube = number * number * number
cube1 = number1 * number1 * number1
cube2 = number2 * number2 * number2
cube3 = number3 * number3 * number3
cube4 = number4 * number4 * number4
cube5 = number5 * number5 * number5
print("number\tsquare\tcube")
print(number, "\t", square, "\t", cube)
print(number1, "\t", square1, "\t", cube1)
print(number2, "\t", square2, "\t", cube2)
print(number3, "\t", square3, "\t", cube3)
print(number4, "\t", square4, "\t", cube4)
print(number5, "\t", square5, "\t", cube5)


#Exercise 2.9(Integer Value of a Character)
print(ord('B'))
print(ord('C'))
print(ord('D'))
print(ord('b'))
print(ord('c'))
print(ord('d'))
print(ord('0'))
print(ord('1'))
print(ord('2'))
print(ord('$'))
print(ord('*'))
print(ord('+'))
print(ord(' '))


#Exercise 2.10 (Arithmetic, Smallest and Largest)
integer1 = int(input("Enter the first integer: "))
integer2 = int(input("Enter the second integer: "))
integer3 = int(input("Enter the third  integer: "))

sum = integer1 + integer2 + integer3
product = integer1 * integer2 * integer3
average = sum / 3
largest = integer1
if integer2 > largest:
    largest = integer2
if integer3 > largest:
    largest = integer3
print("The largest is ", largest)
smallest = integer1
if integer2 < smallest:
    smallest = integer2
if integer3 < smallest:
    smallest = integer3
print("The smallest is ", smallest)


#Exercise 2.11 (Separating the Digits in an Integer)
integer = int(input("Enter a five-digit integer: "))


firstDigit = integer // 10000
secondDigit = (integer % 10000) // 1000
thirdDigit = (integer % 1000) // 100
fourthDigit = (integer % 100) // 10
fifthDigit = (integer % 10)
print(firstDigit, "   ", secondDigit, "   ", thirdDigit, "   ", fourthDigit, "   ", fifthDigit)


#Exercise 2.12 (7% Investment Return) //Do this in java later this evening using loop
principal = 1000
interestRate = 7
nthYear = 10
interest_amount = principal * (1 + interestRate) ** nthYear
print("At the end of 10 years, the amount on deposit is ", interest_amount )
nthYear = 20
interest_amount = principal * (1 + interestRate) ** nthYear
print("At the end of 20 years, the amount on deposit is ", interest_amount)
nthYear = 30
interest_amount = principal * (1 + interestRate) ** nthYear
print("At the end of 30 years, the amount on deposit is ", interest_amount)


#Exercise 2.13 (How big can Python Intgers be?)
#integer = 123456746 ** 123897646
#print(type(integer))


#Exercise 2.14 (Target-Heart Rate Calculator)
age = int(input("Enter your age in years: "))
maximum_heartRate = 220 - age
print("Your maximum heart rate is:", maximum_heartRate, "and your target heartRate is 50 -85% of", age)


#Exercise 2.15 (Sort in Ascending Order)
integer1 = float(input("Enter the first integer: "))
integer2 = float(input("Enter the second integer: "))
integer3 = float(input("Enter the third  integer: "))

smallest = integer1
if integer2 < smallest:
    smallest = integer2
if integer3 < smallest:
    smallest = integer3

largest = integer1
if integer2 > largest:
    largest = integer2
if integer3 > largest:
    largest = integer3

if (integer1 != largest) and (integer1 != smallest):
    median = integer1
if (integer2 != largest) and (integer2 != smallest):
    median = integer2
if (integer3 != largest) and (integer3 != smallest):
    median = integer3
    
print("Your numbers in ascending order:", smallest, median, largest)










