#5.21 (Computer-Assisted Instruction: Reducing Student Fatigue) 


computer_responses = [['Very good!', 'Nice work!', 'Keep up the good work!'], ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']]


import random
def get():
	random_generate_numbers = (random.randrange(0, 11),)
	random_generate_numbers += (random.randrange(0, 11),)
	
	result = random_generate_numbers[0] * random_generate_numbers[1]
	user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
	while(user_response != -1):
		random_number = random.randrange(0, 3)
			
		if user_response == result:
			print(computer_responses[0][random_number])
			random_generate_numbers = (random.randrange(0, 11),)
			random_generate_numbers += (random.randrange(0, 11),)
	
			result = random_generate_numbers[0] * random_generate_numbers[1]
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}?(Enter -1 to exit) '))
			

		else:
			print(computer_responses[1][random_number])
			user_response = int(input(f'How much is {random_generate_numbers[0]} times {random_generate_numbers[1]}? '))
			
		
get()
















