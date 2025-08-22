import random
def addition_difficulty_1():
	random_generate_numbers = (random.randrange(0, 11),)
	random_generate_numbers += (random.randrange(0, 11),)
	
	result = random_generate_numbers[0] + random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} + {random_generate_numbers[1]}? '))
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] + random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} + {random_generate_numbers[1]}?(Enter -1 to exit) '))
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = int(input(f'How much is {random_generate_numbers[0]} + {random_generate_numbers[1]}? '))
			count += 1

def subtraction_difficulty_1():
	random_generate_numbers = (random.randrange(0, 11),)
	random_generate_numbers += (random.randrange(0, 11),)
	
	result = random_generate_numbers[0] - random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}? '))
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] + random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}?(Enter -1 to exit) '))
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}? '))
			count += 1


def multiplication_difficulty_1():
	random_generate_numbers = (random.randrange(0, 11),)
	random_generate_numbers += (random.randrange(0, 11),)
	
	result = random_generate_numbers[0] * random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] * random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}?(Enter -1 to exit) '))
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
			count += 1
		

def division_difficulty_1():
	random_generate_numbers = (random.randrange(1, 11),)
	random_generate_numbers += (random.randrange(1, 11),)
	
	result = random_generate_numbers[0] / random_generate_numbers[1]
	user_response = float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}? '), 2)
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] / random_generate_numbers[1]
			user_response = round(float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}?(Enter -1 to exit) ')), 2)
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = round(float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}? ')), 2)
			count += 1


def multiplication_difficulty_2():
	random_generate_numbers = (random.randrange(10, 100),)
	random_generate_numbers += (random.randrange(10, 100),)
	
	result = random_generate_numbers[0] * random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(10, 100),)
			random_generate_numbers += (random.randrange(10, 100),)
	
			result = random_generate_numbers[0] * random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}?(Enter -1 to exit) '))
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
			count += 1


def addition_difficulty_2():
	random_generate_numbers = (random.randrange(10, 100),)
	random_generate_numbers += (random.randrange(10, 100),)
	
	result = random_generate_numbers[0] + random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(10, 100),)
			random_generate_numbers += (random.randrange(10, 100),)
	
			result = random_generate_numbers[0] + random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} + {random_generate_numbers[1]}?(Enter -1 to exit) '))
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = int(input(f'How much is {random_generate_numbers[0]} + {random_generate_numbers[1]}? '))
			count += 1



def subtraction_difficulty_2():
	random_generate_numbers = (random.randrange(10, 100),)
	random_generate_numbers += (random.randrange(10, 100),)
	
	result = random_generate_numbers[0] - random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}? '))
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(10, 100),)
			random_generate_numbers += (random.randrange(10, 100),)
	
			result = random_generate_numbers[0] - random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}?(Enter -1 to exit) '))
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}? '))
			count += 1


def division_difficulty_2():
	random_generate_numbers = (random.randrange(10, 100),)
	random_generate_numbers += (random.randrange(10, 100),)
	
	result = random_generate_numbers[0] / random_generate_numbers[1]
	user_response = round(float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}? ')), 2)
	count = 1
	while(user_response != -1):
		if user_response == result:
			if count % 2 == 0:
				print("Very good!")
			elif count % 5 == 0 and count % 2 != 0:
				print("Nice Work!")
			else:
				print('Keep up the good work!')
			random_generate_numbers = (random.randrange(10, 100),)
			random_generate_numbers += (random.randrange(10, 100),)
	
			result = random_generate_numbers[0] / random_generate_numbers[1]
			user_response = round(float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}?(Enter -1 to exit) ')), 2)
			count += 1

		else:
			if count % 2 == 0:
				print("No. Please try again.")
			elif count % 5 == 0 and count % 2 != 0:
				print('Wrong. Try once more')
			else:
				print('No. Keep trying')
			user_response = round(float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}? ')), 2)
			count += 1


def random_arithmetic_difficulty_1():
	operator = random.randrange(1, 5)
	match(operator):
		case 1:
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] + random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} added {random_generate_numbers[1]}? '))
			count = 1
			if user_response == result:
				if count % 2 == 0:
					print("Very good!")
				elif count % 5 == 0 and count % 2 != 0:
					print("Nice Work!")
				else:
					print('Keep up the good work!')
				count += 1
				
			else:
				if count % 2 == 0:
					print("No. Please try again.")
				elif count % 5 == 0 and count % 2 != 0:
					print('Wrong. Try once more')
				else:
					print('No. Keep trying')
				user_response = int(input(f'How much is {random_generate_numbers[0]} + {random_generate_numbers[1]}? '))
				count += 1
			random_arithmetic_difficulty_1()

		case 2:
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] - random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} subtract {random_generate_numbers[1]}? '))
			count = 1
			if user_response == result:
				if count % 2 == 0:
					print("Very good!")
				elif count % 5 == 0 and count % 2 != 0:
					print("Nice Work!")
				else:
					print('Keep up the good work!')
				count += 1
				
			else:
				if count % 2 == 0:
					print("No. Please try again.")
				elif count % 5 == 0 and count % 2 != 0:
					print('Wrong. Try once more')
				else:
					print('No. Keep trying')
				user_response = int(input(f'How much is {random_generate_numbers[0]} - {random_generate_numbers[1]}? '))
				count += 1
			random_arithmetic_difficulty_1()
			
		case 3:
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] * random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
			count = 1
			if user_response == result:
				if count % 2 == 0:
					print("Very good!")
				elif count % 5 == 0 and count % 2 != 0:
					print("Nice Work!")
				else:
					print('Keep up the good work!')
				count += 1
				
			else:
				if count % 2 == 0:
					print("No. Please try again.")
				elif count % 5 == 0 and count % 2 != 0:
					print('Wrong. Try once more')
				else:
					print('No. Keep trying')
				user_response = int(input(f'How much is {random_generate_numbers[0]} * {random_generate_numbers[1]}? '))
				count += 1
			random_arithmetic_difficulty_1()
		case 4:
			random_generate_numbers = (random.randrange(1, 10),)
			random_generate_numbers += (random.randrange(1, 10),)
	
			result = round((random_generate_numbers[0] / random_generate_numbers[1]), 1)
			user_response = float(input(f'How much is {random_generate_numbers[0]} divided by {random_generate_numbers[1]}? '))
			count = 1
			if user_response == result:
				if count % 2 == 0:
					print("Very good!")
				elif count % 5 == 0 and count % 2 != 0:
					print("Nice Work!")
				else:
					print('Keep up the good work!')
				count += 1
				
			else:
				if count % 2 == 0:
					print("No. Please try again.")
				elif count % 5 == 0 and count % 2 != 0:
					print('Wrong. Try once more')
				else:
					print('No. Keep trying')
				user_response = int(input(f'How much is {random_generate_numbers[0]} / {random_generate_numbers[1]}? '))
				count += 1
			random_arithmetic_difficulty_1()

