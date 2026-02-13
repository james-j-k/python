class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)

acc1 = BankAccount(1000)
acc2 = BankAccount(500)

acc1.deposit(200)
acc1.show_balance()
