# Welcome Back

# ==========================================
# POLYMORPHISM IN PYTHON
# ==========================================

# ------------------------------------------
# WHAT IS POLYMORPHISM?
# ------------------------------------------
# Polymorphism means "many forms".
# The same method name can perform different actions depending on
# the object being used.

# ------------------------------------------
# SIMPLE POLYMORPHISM
# ------------------------------------------

class Dog:
    def sound(self):
        print("Dog says Woof!")

class Cat:
    def sound(self):
        print("Cat says Meow!")

dog1 = Dog()
cat1 = Cat()

print("----- SIMPLE POLYMORPHISM -----")
dog1.sound()
cat1.sound()

# ------------------------------------------
# POLYMORPHISM USING A FUNCTION
# ------------------------------------------

class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

def make_sound(animal):
    animal.sound()

dog1 = Dog()
cat1 = Cat()

print("\n----- FUNCTION POLYMORPHISM -----")
make_sound(dog1)
make_sound(cat1)

# ------------------------------------------
# POLYMORPHISM WITH A LIST
# ------------------------------------------

class Dog:
    def sound(self):
        print("Dog says Woof!")

class Cat:
    def sound(self):
        print("Cat says Meow!")

class Cow:
    def sound(self):
        print("Cow says Moo!")

animals = [Dog(), Cat(), Cow()]

print("\n----- POLYMORPHISM WITH LIST -----")
for animal in animals:
    animal.sound()

# ------------------------------------------
# POLYMORPHISM WITH INHERITANCE
# ------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")

animal1 = Animal()
dog1 = Dog()
cat1 = Cat()

print("\n----- POLYMORPHISM WITH INHERITANCE -----")
animal1.sound()
dog1.sound()
cat1.sound()

# ------------------------------------------
# BUILT-IN POLYMORPHISM
# ------------------------------------------
# The same built-in function can work with different data types.

print("\n----- BUILT-IN POLYMORPHISM -----")
text = "Hello"
numbers = [10, 20, 30, 40]
print("Length of text:", len(text))
print("Length of list:", len(numbers))

# ==========================================
# ==========================================
# ==========================================
# CHALLENGE : Write a code to create a PAYMENT SYSTEM

# ------------------------------------------
# CREDIT CARD PAYMENT
# ------------------------------------------

class CreditCardPayment:
    def pay(self, amount):
        print(f"Payment of {amount} made using Credit Card.")

# ------------------------------------------
# UPI PAYMENT
# ------------------------------------------

class UPIPayment:
    def pay(self, amount):
        print(f"Payment of {amount} made using UPI.")

# ------------------------------------------
# CASH PAYMENT
# ------------------------------------------
class CashPayment:
    def pay(self, amount):
        print(f"Payment of {amount} made using Cash.")

# ------------------------------------------
# PROCESS PAYMENT FUNCTION
# ------------------------------------------
def process_payment(payment, amount):
    payment.pay(amount)

# ------------------------------------------
# CREATING PAYMENT OBJECTS
# ------------------------------------------
credit_card = CreditCardPayment()
upi = UPIPayment()
cash = CashPayment()
# ------------------------------------------
# PROCESSING PAYMENTS
# ------------------------------------------
print("\n===== PAYMENT SYSTEM =====")
process_payment(credit_card, 1000)
process_payment(upi, 500)
process_payment(cash, 200)
# ==========================================
# ANOTHER PAYMENT EXAMPLE USING A LIST
# ==========================================
payments = [
CreditCardPayment(),
UPIPayment(),
CashPayment()
]
print("\n----- PROCESSING MULTIPLE PAYMENTS -----")
for payment in payments:
    payment.pay(100)

# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day
