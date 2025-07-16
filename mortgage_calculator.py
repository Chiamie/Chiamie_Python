principal = int(input("Enter the amount you wish to borrow: "))
annualRate = float(input("Enter the yearly interest on the loan: "))
loanDuration_Years = int(input("Enter the duraton of the loan in years: "))

PERCENTAGE = 100
MONTHS_IN_YEAR = 12

monthlyRate = annualRate / (PERCENTAGE * MONTHS_IN_YEAR)
loanDuration_Months = loanDuration_Years * MONTHS_IN_YEAR

monthlyPayment_Value = principal * ((monthlyRate * ((1 + monthlyRate) ** loanDuration_Months)) / (((1 + monthlyRate) ** loanDuration_Months) - 1))
print("Your monthly payment value is ", monthlyPayment_Value )