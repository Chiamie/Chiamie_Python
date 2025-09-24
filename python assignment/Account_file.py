import re
from decimal import Decimal

class Account:

    def __init__(self, name, date_of_birth, balance):

        self.name = ""
        self.balance = 0
        self.date_of_birth = ""
        self.set_name(name)
        self.deposit(balance)
        self.set_date(date_of_birth)

    def deposit(self, amount):
        if not isinstance(amount, int):
            raise ValueError("amount must be a number")
        if amount <= Decimal("0.00"):
            raise ValueError("Amount cannot be less or equal to zero")
        if isinstance(amount, float):
            raise ValueError("We dont deposit coin")

        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than balance")
        elif amount < Decimal("0.00"):
            raise ValueError("Amount cannot be less than zero")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_date(self):
        return self.date_of_birth

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.contact

    def get_name(self):
        return self.name

    def set_name(self, customer_name):
        if not isinstance(customer_name, str):
            raise ValueError("customer_name must be a string")

        if not customer_name.isalpha():
            raise ValueError("customer_name must be an alphabet")
        self.name = customer_name


    def set_address(self, address):
        self.address = address
    def set_contact(self, contact):
        self.contact = contact

    def set_date(self, date_of_birth):
        pattern = r'^(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[012])[/-]\d{4}$'
        if not re.fullmatch(pattern, date_of_birth):
            raise ValueError("Date must be in the format DD-MM-YYYY")
        self.date_of_birth = date_of_birth
















