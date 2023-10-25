class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        amount = 1000
        balance = 100 + 1000
        print(f'Amount deposited: ${amount}.00 New Balance: ${balance}.00')
    
    def widthdraw(self, amount):
        amount = 1250
        balance = 1000
        if amount < balance:
            balance = 1000 - 450
            print(f'Amount withdrawn: ${amount}.00 new balance: ${balance}.00')
        if amount > balance:
            balance = 1000 - 10
            print("Insufficient funds.")

    def get_balance(self, balance):
        balance = 990
        print(f'Account Balance: ${balance}.00')
        return f'${balance}.00'
    
    def add_interest(self):
        balance = 990
        interest = 990 *  0.00083
    
    def print_statment(self):
        print(self.full_name)
        print(f'Account No.: {self.account_number}')
        print(f'Balance: {self.balance}')



joi_bank_account = BankAccount("Joi Anderson", "****5678", "$990.00")

print(joi_bank_account.deposit('amount'))
print(joi_bank_account.widthdraw('amount'))
print(joi_bank_account.get_balance('balance'))
print(joi_bank_account.add_interest())
print(joi_bank_account.print_statment())

# print(f"Account No.: ****{str(self.account_number)[4:]}")

# in my case, account_number is an int. so I first convert it to a string, and slice the string to only show the last four digits.