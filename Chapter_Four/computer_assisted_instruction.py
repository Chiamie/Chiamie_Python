# 4.14 (Computer-Assisted Instruction)
import random
def get():
	random_generate_numbers = (random.randrange(0, 11),)
	random_generate_numbers += (random.randrange(0, 11),)
	
	result = random_generate_numbers[0] * random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
	while(user_response != -1):
		if user_response == result:
			print("Very good!")
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] * random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
			

		else:
			print("No. Please try again.")
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
		
get()
