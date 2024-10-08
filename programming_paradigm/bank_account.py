class BankAccount:
  def __init__(self, initial_balance):
    initial_balance = 0
    self.account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.account_balance += amount
      print (f"Deposited: {amount}")
    else:
      print("invalid value")
  def withdraw(self,amount):
    if amount > 0 and amount <= account_balance:
      self.account_balance -= amount
      print (f"your balance is {amount}")
      return True
    else:
      print("Invalid")
      return False
  def display_balance (self,amount):
    print(f"Current Balance: {self.account_balance}")
