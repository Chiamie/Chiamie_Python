#4.10: Guess The Number
import random

guess_number = random.randrange(1, 1000)

user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
print(guess_number)
while user_guess != guess_number:
	if user_guess < guess_number:
		print("Too low. Try again.")
	elif user_guess > guess_number:
		print("Too high. Try again.")
	print(guess_number)
	user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
print("Congratulations!")
	


	
	

