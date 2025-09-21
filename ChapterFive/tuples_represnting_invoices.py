from operator import itemgetter
from decimal import Decimal

def displaylines():
	print("=" * 100)


a_list_of_invoice_tuples = [(83, "Electric sander", 7, 57.98), (24, "Power saw", 18, 99.99),
(7, "Sledge hammer", 11, 21.50), (77, "Hammer", 76, 11.99),
(39, "Jig saw", 3, 79.50)]

#5.15a: Used sorted in built function to arrange the invoice by description in the invoice in ascending order
tuples_invoice_by_des = sorted(a_list_of_invoice_tuples, key = itemgetter(1))
print(tuples_invoice_by_des)
displaylines()

		

			
	
