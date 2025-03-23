class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self._balance


account = BankAccount(100)

# Accessing the balance attribute directly
print(account._balance)  # Output: 100

# Accessing the balance attribute via the getter method
print(account.get_balance())  # Output  100

# Depositing some money
account.deposit(50)
print(account.get_balance())  # Output: 150

# Withdrawing some money
account.withdraw(30)
print(account.get_balance())  # Output: 120

# Trying to withdraw more money than the account balance
try:
    account.withdraw(200)
except ValueError as e:
    print(e)  # Output: Insufficient funds

print(account.get_balance())  # Output: 120

# Trying to access the balance attribute directly

try:
    print(account._balance)
except AttributeError as e:
    print(e)  # Output: 'BankAccount' object has no attribute '_balance'

