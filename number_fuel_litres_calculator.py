total_user_budget = int(input("What is your total fuel budget? "))
PRICE_PER_LITRE = 855
number_fuel_litres = total_user_budget / PRICE_PER_LITRE
print("Your budget can get you", number_fuel_litres, "litres of fuel")