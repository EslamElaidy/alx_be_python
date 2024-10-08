class BankAccount:
  def __init__(self, initial_balance):
    initial_balance = 0
    self.account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.account_balance += amount
      print (f"your balance is {amount}")
    else:
      print("invalid value")
  def withdraw(self,amount):
    if amount > 0 and amount <= account_balance
    self.account_balance -= amount
    print (f"your balance is {amount}")
