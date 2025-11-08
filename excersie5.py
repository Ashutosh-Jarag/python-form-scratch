class Account:
    def __init__(self, accno, balance):
        self.accno = accno
        self.balance = balance
        
    def debit(self, amount):
        self.balance -= amount
        print("Debit of", amount, "is successful")
        
    def credit(self, amount):
        self.balance += amount
        print("Credit of", amount, "is successful")
        
    def showbalance(self):
        print("Balance is:", self.balance)

# Creating an account instance
acc1 = Account(1001, 3000)
print(acc1.accno, acc1.balance)

# Testing the methods
acc1.showbalance()
acc1.credit(500)
acc1.showbalance()
acc1.debit(200)
acc1.showbalance()