two_by_three_list = [[0]*3 for _ in range(2)]
integer = 50
for index in range(2):
	for number in range(3):
		two_by_three_list[index][number] = integer
		integer += 1
		
print(two_by_three_list)