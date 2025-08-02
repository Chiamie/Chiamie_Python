#Loop through 0 to 50; for every even get the square while for every odd get the cube
for number in range(51):
	if number % 2 == 0:
		print(number** 2, end= ' ')
	else:
		print(number** 3, end= ' ')