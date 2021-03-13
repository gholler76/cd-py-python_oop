class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        # self.display_user_balance()

    def transfer_money(self, other_user, amount):
        self.receiver = other_user
        self.transfer = amount
        self.account_balance -= amount
        self.receiver.account_balance += amount
        # self.display_user_balance()

    def display_user_balance(self):
        print(f'{self.name} has ${self.account_balance} in his account.')


Manny = User("Manny", "123@abc.com")
Moe = User("Moe", "456@dff.com")
Jack = User("Jack", "789@ghi.com")

# Manny.make_deposit(800)
# Manny.make_deposit(400)
# Manny.make_deposit(100)
# Manny.make_withdrawal(500)

# Moe.make_deposit(900)
# Moe.make_deposit(200)
# Moe.make_withdrawal(100)
# Moe.make_withdrawal(350)

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

Moe.make_deposit(900)
Moe.make_deposit(200)
Moe.make_withdrawal(100)
Moe.make_withdrawal(350)
Moe.display_user_balance()

# (Jack.make_deposit(1500)
#     .make_withdrawal(500)
#     .make_withdrawal(400)
#     .make_withdrawal(950)
#     .display_user_balance())
