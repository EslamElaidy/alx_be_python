class BankAccount:
  def __init__(self, initial_balance):
    initial_balance = 0
    self.account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.account_balance += amount
    else:
      print("invalid value")
  def withdraw(self,amount):
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      print("Insufficient funds.")
  def display_balance (self,amount):
    print(f"Current Balance: ${self.amount}")
