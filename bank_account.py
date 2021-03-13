class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def acct_deposit(self, amount):
        self.deposit = amount
        self.balance += amount
        return self

    def acct_withdrawal(self, amount):
        self.withdrawal = amount
        self.balance - amount
        return self
    # def display_acct_info(self):

    #     # before save
    #     print(
    #         f"Account Name: {self}, Balance: {self.balance}, Interest Rate: {self.int_rate}.")
    #     # after save
    #     print(
    #         f"Account Name: {self}, Balance: {self.balance}, Interest Rate: {self.int_rate}.")

    def acct_yield_increase(self):
        self.yield_increase = self.balance * self.int_rate
        self.balance = self.balance + self.yield_increase
        return self
# ---


class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit = amount
        self.account.balance += amount
        return self
        # print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdrawal = amount
        self.account.balance -= amount
        return self
        # self.display_user_balance()

    def transfer_money(self, other_user, amount):
        self.receiver = other_user
        self.transfer = amount
        self.account.balance - amount
        self.receiver.account.balance + amount
        return self
        # self.display_user_balance()

    def display_user_balance(self):
        print(
            f'{self.name} has ${self.account.balance} in his account.')
        return self
# ---


Manny = User("Manny", "123@abc.com")
Moe = User("Moe", "456@dff.com")
Jack = User("Jack", "789@ghi.com")

# Manny.make_deposit(500)
# print(Manny.balance)
# Moe.make_deposit(700)
# Jack.make_deposit(1000)


Moe.make_deposit(900).make_deposit(1100).make_deposit(
    1100).make_withdrawal(1500).display_user_balance()


# Jack.make_deposit(1500)
# Jack.make_withdrawal(500)
# Jack.make_withdrawal(400)
# Jack.make_withdrawal(950)

# Manny.transfer_money(Jack, 400)
# Jack.display_user_balance()

# all entries below chained as per "chaining methods" assignment

# Manny.make_deposit(800).make_deposit(400)
# .make_deposit(100).make_withdrawal(
#     500).transfer_money(Jack, 400).display_user_balance())

# (
#     Moe.make_deposit(900)
#     .make_deposit(200)
#     .make_withdrawal(100)
#     .make_withdrawal(350)
#     .display_user_balance()
# )

# (Jack.make_deposit(1500)
#     .make_withdrawal(500)
#     .make_withdrawal(400)
#     .make_withdrawal(950)
#     .display_user_balance())
