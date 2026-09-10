# Welcome Back

# ==========================================
# ENCAPSULATION IN PYTHON
# ==========================================

# ------------------------------------------
# WHAT IS ENCAPSULATION?
# ------------------------------------------
# Encapsulation means:
# 1. Keeping data and methods together inside a class.
# 2. Controlling how data is accessed or modified.

# ------------------------------------------
# PUBLIC VARIABLES
# ------------------------------------------
# Public variables can be accessed and modified directly 
# from outside the class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 18)

print("----- PUBLIC VARIABLES -----")
print("Name:", student1.name)
print("Age:", student1.age)

# We can also modify public variables directly
student1.age = 19
print("Updated Age:", student1.age)

# ------------------------------------------
# PROTECTED VARIABLES
# ------------------------------------------
# Protected variables use a single underscore.
# Example:
# self._name
# This is only a convention in Python. It can be changed though.
# It tells other programmers:
# "This variable should not normally be accessed directly outside 
# the class."

class Person:
    def __init__(self, name):
        self._name = name

person1 = Person("Priya")

print("\n----- PROTECTED VARIABLES -----")
print("Name:", person1._name)

# ------------------------------------------
# PRIVATE VARIABLES
# ------------------------------------------
# Private variables use double underscores.
# Example:
# self.__balance
# Python makes direct access more difficult using a feature 
# called name mangling.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        # Private variable
        self.__balance = balance

account1 = BankAccount("Rahul", 5000)

print("\n----- PRIVATE VARIABLES -----")
print("Account Holder:", account1.account_holder)

# This will cause an error:
# print(account1.__balance)

# ------------------------------------------
# GETTER METHOD
# ------------------------------------------
# A getter method allows us to access private data safely.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def get_balance(self):
        return self.__balance

account1 = BankAccount("Rahul", 5000)

print("\n----- GETTER METHOD -----")
print("Balance:", account1.get_balance())

# ------------------------------------------
# SETTER METHOD
# ------------------------------------------
# A setter method allows us to update private data with validation.

class BankAccount:
    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print("Balance updated successfully.")
        else:
            print("Balance cannot be negative.")

account1 = BankAccount("Priya", 5000)

print("\n----- SETTER METHOD -----")
account1.set_balance(7000)

print("Balance:", account1.get_balance())
account1.set_balance(-100)

# ------------------------------------------
# DEPOSIT METHOD
# ------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Deposit amount must be greater than zero.")
    def get_balance(self):
        return self.__balance

account1 = BankAccount("Amit", 5000)

print("\n----- DEPOSIT METHOD -----")
account1.deposit(1000)

print("Balance:", account1.get_balance())

# ------------------------------------------
# WITHDRAW METHOD
# ------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")
    def get_balance(self):
        return self.__balance

account1 = BankAccount("Rahul", 5000)

print("\n----- WITHDRAW METHOD -----")
account1.withdraw(2000)

print("Balance:", account1.get_balance())

# ------------------------------------------
# USING @property
# ------------------------------------------
# @property allows us to access a method like an attribute.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    @property
    def marks(self):
        return self.__marks

student1 = Student("Priya", 85)

print("\n----- @PROPERTY -----")
print("Marks:", student1.marks)

# ==========================================
# ==========================================
# ==========================================
# CHALLENGE: Create a BANK ACCOUNT MANAGEMENT SYSTEM
# It should contain a class BankAccount:
#   1. __init__- For setting the name and balance(private)
#   2. display_account - Displays Details
#   3. get_balance - Displays balance
#   4. deposit - Updates balance
#   5. Withdraw - Updaes balance

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        # Private balance
        self.__balance = balance
    # --------------------------------------
    # DISPLAY ACCOUNT DETAILS
    # --------------------------------------
    def display_account(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)
    # --------------------------------------
    # GET BALANCE
    # --------------------------------------
    def get_balance(self):
        return self.__balance
    # --------------------------------------
    # DEPOSIT MONEY
    # --------------------------------------
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.__balance += amount
            print("Deposit successful!")
            print("New Balance:", self.__balance)
    # --------------------------------------
    # WITHDRAW MONEY
    # --------------------------------------
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")
            print("New Balance:", self.__balance)
# ------------------------------------------
# CREATING BANK ACCOUNT OBJECT
# ------------------------------------------
account1 = BankAccount("Rahul", 5000)
# ------------------------------------------
# DISPLAY INITIAL DETAILS
# ------------------------------------------
print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
account1.display_account()
# ------------------------------------------
# DEPOSIT MONEY
# ------------------------------------------
print("\nDepositing 1000...")
account1.deposit(1000)
# ------------------------------------------
# WITHDRAW MONEY
# ------------------------------------------
print("\nWithdrawing 2000...")
account1.withdraw(2000)
# ------------------------------------------
# TRY INVALID WITHDRAWAL
# ------------------------------------------
print("\nTrying to withdraw 10000...")
account1.withdraw(10000)
# ------------------------------------------
# FINAL BALANCE
# ------------------------------------------
print("\n----- FINAL BALANCE -----")
print("Balance:", account1.get_balance())
# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day