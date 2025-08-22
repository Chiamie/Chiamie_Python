#4.17 (Computer-Assisted Instruction: Varying the Types of Problems)
import operations_function



menu = """
	Welcome to Chiamie ClassRoom
	Choose the Multiplication learning level of your choice
	1. Difficulty level 1
	2. Difficulty level 2
	"""
user_response = int(input(menu))
match(user_response):
	case 1:
		type_of_arithmetics = """
		1. Addition
		2. Subtraction
		3. Multiplication
		4. Division
		5. Random Arithmetic
		"""
		user_response = int(input(type_of_arithmetics + "Select which mathematical operation you want to practice:"))
		match(user_response):
			case 1:
				operations_function.addition_difficulty_1()
			case 2:
				operations_function.subtraction_difficulty_1()
			case 3:
				operations_function.multiplication_difficulty_1()
			case 4:
				operations_function.division_difficulty_1()
			case 5:
				operations_function.random_arithmetic_difficulty_1()
			
	








