class BankAccount:
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount}.00 -> New Balance: ${self.balance}.00')
    
    def widthdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}.00 -> New balance: ${self.balance}.00')

    def get_balance(self, balance):
        print(f'Welcome! Your Account Available Balance is: ${balance}.00')
        return self.balance
    
    def add_interest(self):
        interest = self.balance *  0.00083
        self.balance += interest
    
    def print_statment(self):
        print(f"{self.full_name}")
        print(f"Account No.: {self.account_number}")
        print(f"Balance: {self.balance}")


mitchell_bank_account = BankAccount("Mitchell", "03141592")
mitchell_bank_account.deposit(400000)
mitchell_bank_account.print_statment()
mitchell_bank_account.widthdraw(150)
mitchell_bank_account.print_statment()

# print(f"Account No.: ****{str(self.account_number)[4:]}")

# in my case, account_number is an int. so I first convert it to a string, and slice the string to only show the last four digits.