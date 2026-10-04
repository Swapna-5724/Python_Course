#   Question -> 01
#   Create Account class with 2 attributes - balance and account no.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc


acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)


#   Question -> 02
#   Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("total balance = ", self.get_balance())

    def get_balance(self):
         return self.balance


# acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)