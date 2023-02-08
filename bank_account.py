class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 100): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee{self.balance}")
            self.balance -= 5
        return self
    
        # your code here
    def display_account_info(self):
        print("Balance: ", self.balance)
        return self
        # your code here
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

Bob = BankAccount(.01)
Bob.deposit(300).deposit(200).deposit(100).withdraw(450).yield_interest().display_account_info()

Christian = BankAccount(.2)
Christian.deposit(300).deposit(200).withdraw(50).withdraw(150).withdraw(70).withdraw(55).yield_interest().display_account_info()
