class Bank_account:
    def __init__(self, full_name, account_number, total_balance):
        self.name = full_name
        self.account = account_number
        self.balance = total_balance #should start at 0, do I make this =0?

    def deposit(self, amount):
        new_balance = amount + self.balance
        self.balance = new_balance
        return f'Amount deposited: ${amount} Your new balance is: ${new_balance}'

    def withdraw(self, amount):
        new_balance = self.balance - amount

        if amount > self.balance:
            overdraft = new_balance - 10
            self.balance = overdraft
            return f'Insufficient funds. You have been charged a $10 overdraft fee. Your balance is now ${overdraft}.'
        else:
            self.balance = new_balance
            return f'Amount withdrawn: ${amount} Your new balance is: ${new_balance}' 

    def get_balance(self):
        return f'Your current account balance is ${self.balance}'

    def add_interest(self):
        interest = self.balance * 0.00083
        new_balance = self.balance + interest
        self.balance = new_balance
        return f'${interest} in interest was added to your account this month. You current balance is now ${self.balance}'

    def print_statement(self):
        sliced = slice(4, 8)
        ending_numbers = self.account[sliced]
        return f' {self.name} \n Account No.: ****{ending_numbers} \n Balance: ${self.balance}'

