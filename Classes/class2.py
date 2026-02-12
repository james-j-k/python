class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
acc1 = BankAccount(1000)
acc2 = BankAccount(500)

acc1.deposit(200)

print(acc1.balance)  # 1200
print(acc2.balance)  # 500