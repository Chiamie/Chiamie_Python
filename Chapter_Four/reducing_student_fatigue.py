#4.15 (Computer-Assisted Instruction: Reducing Student Fatigue)

import random
def get():
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
		
get()

