#3.21 (Calculate Change Using Fewest Number of Coins) 
purchase_price_in_cents = 27
purchaser_payment_in_cents = 100
A_DIME_IN_CENT = 10
A_QUARTER_IN_CENT = 25
A_PENNY_IN_CENT = 1



balance_cents = purchaser_payment_in_cents - purchase_price_in_cents 
balance_in_quarters = balance_cents // A_QUARTER_IN_CENT

remaining = balance_cents - (balance_in_quarters * 25)
balance_in_dimes = remaining // A_DIME_IN_CENT 
remaining = remaining  - (balance_in_dimes * 10)
balance_in_penny = remaining  // A_PENNY_IN_CENT 

 
print("""
 Your change is:""",
 balance_in_quarters, "quarters",
 balance_in_dimes, "dimes",
 balance_in_penny, "pennies" )