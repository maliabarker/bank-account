class Bank_account:
    def __init__(self, full_name, account_number, account_type):
        self.name = full_name
        self.account = account_number
        self.balance = 0 #should start at 0, do I make this =0?
        self.type = account_type

    def deposit(self, amount):
        new_balance = amount + self.balance
        self.balance = new_balance
        return f'Amount deposited: ${amount:.2f} Your new balance is: ${new_balance:.2f}'

    def withdraw(self, amount):
        new_balance = self.balance - amount

        if amount > self.balance:
            overdraft = new_balance - 10
            self.balance = overdraft
            return f'Insufficient funds. You have been charged a $10.00 overdraft fee. Your balance is now ${overdraft:.2f}.'
        else:
            self.balance = new_balance
            return f'Amount withdrawn: ${amount:.2f} Your new balance is: ${new_balance:.2f}' 

    def get_balance(self):
        return f'Your current account balance is ${self.balance:.2f}'

    def add_interest(self):
        if self.type == "Checking":
            interest = round(self.balance * 0.00083, 2)
            new_balance = self.balance + interest
            self.balance = new_balance
            return f'${interest:.2f} in interest was added to your account this month. You current balance is now ${self.balance:.2f}'
        elif self.type == "Savings":
            interest = round(self.balance * 0.01, 2)
            new_balance = self.balance + interest
            self.balance = new_balance
            return f'${interest:.2f} in interest was added to your account this month. You current balance is now ${self.balance:.2f}'

    def print_statement(self):
        sliced = slice(4, 8)
        ending_numbers = self.account[sliced]
        return f' {self.name} \n Account No.: ****{ending_numbers} \n Balance: ${self.balance:.2f}'

marlie_account = Bank_account("Marlie Gibson", "01234567", "Checking")
malia_account = Bank_account("Malia Barker", "28374659", "Savings")
dog_account = Bank_account("Sydney Barkerson", "80808080", "Checking")
mitchell_account = Bank_account("Mitchell Hudson", "3141592", "Savings")

print(marlie_account.balance)
print(marlie_account.deposit(100))
print(marlie_account.withdraw(20))
print(marlie_account.balance)
print(marlie_account.add_interest())
print(marlie_account.print_statement())

print('--------------------------------------')

print(malia_account.balance)
print(malia_account.deposit(20))
print(malia_account.withdraw(30))
print(malia_account.get_balance())
print(malia_account.deposit(50))
print(malia_account.add_interest())
print(malia_account.print_statement())

print('--------------------------------------')

print(dog_account.get_balance())
print(dog_account.deposit(2000))
print(dog_account.add_interest())
print(dog_account.get_balance())
print(dog_account.add_interest())
print(dog_account.print_statement())

print('--------------------------------------')
print(mitchell_account.deposit(400000))
print(mitchell_account.print_statement())
print(mitchell_account.add_interest())
print(mitchell_account.print_statement())
print(mitchell_account.withdraw(150))
print(mitchell_account.print_statement())


