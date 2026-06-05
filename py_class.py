# Python Constructor

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_details(self):
        print(f"Account Holder:", self.name, "with balance", self.balance)
        print(f"Balance:", self.balance)

# Creating Objects
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)

# Calling Methods
account1.show_details()
account2.show_details() 