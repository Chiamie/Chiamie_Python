#4.16 (Computer-Assisted Instruction: Difficulty Levels)


import random
def difficulty_1():
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
		


def difficulty_2():
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


menu = """
	Welcome to Chiamie ClassRoom
	Choose the Multiplication learning level of your choice
	1. Difficulty level 1
	2. Difficulty level 2
	"""
user_response = int(input(menu))
match(user_response):
	case 1:
		difficulty_1()
	case 2:
		difficulty_2()








