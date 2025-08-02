#Exercise 2.12 (7% Investment Return)
principal = 1000
PERCENT = 100
interestRate = 7 / PERCENT


for number in range(1, 31,):
	interest_amount = principal * (1 + (interestRate)) ** number
	print(f"{interest_amount: .2f}", end= " ")
