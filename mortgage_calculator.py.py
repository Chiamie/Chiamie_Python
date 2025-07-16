principal = int(input("Enter the amount you wish to borrow: "))
annualRate = float(input("Enter the yearly interest on the loan: "))
loanDuration_Years = int(input("Enter the duraton of the loan in years: "))

monthlyRate = annualRate / (100 * 12)
loanDuration_Months = loanDuration_Years * 12

monthlyPayment_Value = principal * ((monthlyRate * ((1 + monthlyRate) ** loanDuration_Months)) / (((1 + monthlyRate) ** loanDuration_Months) - 1))
print("Your monthly payment value is ", monthlyPayment_Value )