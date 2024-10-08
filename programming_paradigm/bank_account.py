class BankAccount:
  def __init__(self, initial_balance):
    initial_balance = 0
    self.account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.account_balance += amount
      print (f"Deposited: ${amount:.f}")
    else:
      print("invalid value")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.account_balance:
      self.account_balance -= amount
      print (f"Withdrew: ${amount:.2f}")
      return True
    else:
      print("Insufficient funds.")
      return False
  def display_balance (self,amount):
    print(f"Current Balance: ${self.account_balance:.2f}")
