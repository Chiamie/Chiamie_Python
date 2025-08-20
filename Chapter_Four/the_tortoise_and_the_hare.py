#4.12: Simulation: The Tortoise and the Hare
import random

guess_number = random.randrange(1, 1000)

user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
print(guess_number)
count = 0
while user_guess != guess_number:
	if user_guess < guess_number:
		print("Too low. Try again.")
	elif user_guess > guess_number:
		print("Too high. Try again.")
	print(guess_number)
	count += 1
	if count <= 10:
		print("Either you know the secret or you got lucky!")
	elif count > 10:
		print("You should be able to do better!")
	user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
print("Congratulations!")
	


	
	











