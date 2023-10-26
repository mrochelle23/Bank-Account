# Bank Account

This application uses Python attributes and methods within objects to create a functioning bank account to: deposit money, withdraw money, add monthly interest, and display the users full name, account number, and current account balance when money is deposited and after money is withdrawn.

## Installation

Well start off by
1. Making a directory
2. Adding a python virtual environment
3. Initializing a git and GitHub repos

Start by making a directory
```bash
$ mkdir bank-account
```

Next, setup your Virtual Environment.

If you haven't setup a virtual environment before, make sure install it with the command ```python3 -m pip install --user virtualenv```

Otherwise, make sure you are in the main directory of the project and run the following to create your virtualenv:
```bash 
$ python3 -m venv env
$ source env/bin/activate
```

We can also setup our GitHub repository before we go any futher.

Run the following commands in the main project directory and then follow the interactive prompts:
```bash
$ git init -b main
$ gh repo create bank-account
```

Ok! Now we are ready to start making a little code.

Let's make a simple class called Dog.

Make the file ```bankaccount.py```

```bash
$ touch bankaccount.py
```
Now define a ```class``` using the class keyword in Python, and we're going to add 2 property to the BankAccount class called ```full_name``` and ```account_number```:


```python
#bankaccount.py
class BankAccount:
def__init__(self, full_name, account_number):
   self.full_name = full_name
   self.account_number = account_number
   self.balance = 0
```

Hang on, what's that __init__ method? And what does self refer to? Let's take a brief moment to discuss both of these:

## init

This is a required method that every class must have. ```__init__``` describes how to create an object based on the blueprint provided by the class. It's a special method called a constructor, which runs whenever a new instance of the class is created. We mainly use it to assign values to our properties. In this case, we take the value of ```name``` and assign it to ```self.full_name``` so that we can reference it for that object. But what does self mean?

## Self

self is a keyword used in classes to refer to the specific object built from the class. If we created 100 BankAccount objects, how does each account know what the values of its own properties are? Is the user trying to deposit? Is the user trying to withdraw money? The ```self``` keyword allows an object to keep track of its own properties, separate from any other object of the same class. It is also a required property to every method within a class, so make sure to always have it as the first property to any method in a class that you create.

## Add an Instance Method

A class has really two parts: properties (variables) which you've seen, and methods (functions) that that an instance of that class can do.

What are some actions the user can take? How about depositing money? What other actions can the user do?

Let's define our first method called ```deposit```. This will let us call something like this: ```mitchell_bank_account.depsit(self, amount)```. And then we can have ```self.balance += amount``` and print
```print(f'Amount deposited: ${amount}.00 -> New Balance: ${self.balance}.00')```

The user can also withdraw money but if they try to withdraw more than the current available balance is, they will get a "Insuffienct funds" message and be charged a $10 fee

```python
def widthdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}.00 -> New balance: ${self.balance}.00')
```

The user will also be able to get their available balance after withdrawing money

```python
def widthdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}.00 -> New balance: ${self.balance}.00')
```

Now, the User will also have annual interest of 1%, which is 0.083% per month:

```python
def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
```

And Now the user will have a full description
of their full name, the last four digits of their account number, and their current balance

```python
def print_statment(self):
        print(f"{self.full_name}")
        print(f"Account No.: {self.account_number}")
        print(f"Balance: {self.balance}")
```

## Make an Instance of the BankAccount Class

Now to use this Class or blueprint of a BankAccount, we have to run it, which saves it into memory and allows us to use it to make instances of the BankAccount class, called instances. As we said before, the process of creating an object in memory from the class definition is called instantiation. Let's make an instance of the BankAccount class:

```python
mitchell_bank_account = BankAccount("Mitchell", "03141592")
```
We now want to print the steps he took to deposit money, withdraw money, and view his account info

```python
#mitchell wants to deposit $400,000 and see that as his new account balance
mitchell_bank_account.deposit(400000)
# He now want to see all of this account information
mitchell_bank_account.print_statement()
#mitchell wants to withdraw $150 to go buy a new pair of Yeezys
mitchell_bank_account.withdraw(150)
# He now want to see his new account balance after the withdraw
mitchell_bank_account.print_statement()
```

## Stretch Challenge

Try to create other users that include:
1. Different names
2. Different account number
3. Different amounts deposited
4. Different amounts withdrawn
5. Have at least one user that withdraws too much and is charged a $10 fee and prints an Insuffient funds message

## Strech Challenge Solutions
This creates two new users who are all depositing different amounts, withdrawing amounts and 
```python
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
        interest = self.balance * 0.00083
        self.balance += interest
    
    def print_statment(self):
        print(f"{self.full_name}")
        print(f"Account No.: {self.account_number}")
        print(f"Balance: {self.balance}.00")


mitchell_bank_account = BankAccount("Mitchell", "03141592")
mitchell_bank_account.deposit(400000)
mitchell_bank_account.print_statment()
mitchell_bank_account.widthdraw(150)
mitchell_bank_account.print_statment()
print("___________________________________________________")

joi_bank_account = BankAccount("Joi Anderson", "****5678")
joi_bank_account.deposit(1000)
joi_bank_account.print_statment()
joi_bank_account.widthdraw(100)
joi_bank_account.print_statment()
print("___________________________________________________")

john_bank_account = BankAccount("John Smith", "****7845")
john_bank_account.deposit(4000)
john_bank_account.print_statment()
john_bank_account.widthdraw(200)
john_bank_account.print_statment()
print("___________________________________________________")

cody_bank_account = BankAccount("Cody Jenkins", "****5649")
cody_bank_account.deposit(5000)
cody_bank_account.print_statment()
cody_bank_account.widthdraw(6500)
cody_bank_account.print_statment()
```

## Commit

Commit your work to GitHub. Feel free to use a custom message of your own, as long as it accurately describes what you did.
```bash
$ git add . && git commit -m "Created Mitchell's Bank Account" && git push
``` 

