
class Bankaccount:

    def __init__(self, balance, deposit):
        self.balance = balance
        self.deposit = deposit


    def money_deposit(self):
        self.balance = self.balance + self.deposit
        print(f"Balance is = {self.balance}")

    def money_withdraw(self):
        withdraw = int(input("Enter the amount you want to withdraw from bank : "))
        if withdraw > self.balance:
            print("Your money withdrawal request has been denied")
        else:
            self.balance = self.balance - withdraw

        print(f"New Balance is {self.balance}")

bal = Bankaccount(1000000, 100000)
bal.money_deposit()
bal.money_withdraw()



