# Welcome Back !

# ==========================================
#        INHERITANCE IN PYTHON
# ==========================================

# ------------------------------------------
# WHAT IS INHERITANCE?
# ------------------------------------------
# Inheritance allows a child class to use
# the attributes and methods of a parent class.

# Parent Class = Base Class
# Child Class  = Derived Class

# ------------------------------------------
# SINGLE INHERITANCE
# ------------------------------------------

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog1 = Dog()

print("----- SINGLE INHERITANCE -----")
dog1.eat()      # Inherited from Animal
dog1.bark()     # Belongs to Dog

# ------------------------------------------
# INHERITING ATTRIBUTES
# ------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying")

student1 = Student("Rahul")

print("\n----- INHERITED ATTRIBUTES -----")
student1.display_name()
student1.study()

# ------------------------------------------
# USING super()
# ------------------------------------------
# super() is used to call methods or the
# constructor of the parent class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        # Calling parent constructor
        super().__init__(name, age)
        self.marks = marks

student1 = Student("Priya", 18, 85)

print("\n----- super() FUNCTION -----")
print("Name:", student1.name)
print("Age:", student1.age)
print("Marks:", student1.marks)

# ------------------------------------------
# MULTILEVEL INHERITANCE
# ------------------------------------------
# Grandparent
# ↓
# Parent
# ↓
# Child

class Grandparent:
    def house(self):
        print("Grandparent owns a house")

class Parent(Grandparent):
    def car(self):
        print("Parent owns a car")

class Child(Parent):
    def bike(self):
        print("Child owns a bike")

child1 = Child()

print("\n----- MULTILEVEL INHERITANCE -----")
child1.house()
child1.car()
child1.bike()

# ------------------------------------------
# MULTIPLE INHERITANCE
# ------------------------------------------
# A child class inherits from
# more than one parent class.

class Father:
    def skills_from_father(self):
        print("Skills inherited from father")

class Mother:
    def skills_from_mother(self):
        print("Skills inherited from mother")

class Child(Father, Mother):
    def own_skills(self):
        print("Child has their own skills")

child1 = Child()

print("\n----- MULTIPLE INHERITANCE -----")
child1.skills_from_father()
child1.skills_from_mother()
child1.own_skills()

# ------------------------------------------
# METHOD OVERRIDING
# ------------------------------------------
# A child class can create its own version
# of a method from the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")

dog1 = Dog()
cat1 = Cat()

print("\n----- METHOD OVERRIDING -----")
dog1.sound()
cat1.sound()

# ------------------------------------------
# CALLING PARENT METHOD USING super()
# ------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        # Calling parent method
        super().sound()
        print("Dog says Woof!")

dog1 = Dog()

print("\n----- PARENT METHOD WITH super() -----")
dog1.sound()

# ==========================================
# ==========================================
# ==========================================
# CHALLENGE - Write a code to create a Vehicle
# Management System
# It should have :
#   1. Vehicle parent class
        #display_detail function which shows brand and model
#   2. Car child class
#       #Displays All attributes of Vehicle and no. of doors 
        #Hint - Use super() 
#   3. Bike child class
        #Displays ALl attributes of Vehicle and bike type
#   4. Create two objects and pass them to the class and display 
#       the details

# ------------------------------------------
# PARENT CLASS
# ------------------------------------------
class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
# ------------------------------------------
# CHILD CLASS - CAR
# ------------------------------------------

class Car(Vehicle):

    def __init__(self, brand, model, number_of_doors):
        # Call parent constructor
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors

    def display_details(self):
        print("\n----- CAR DETAILS -----")
        # Call parent method
        super().display_details()
        print("Number of Doors:", self.number_of_doors)
# ------------------------------------------
# CHILD CLASS - BIKE
# ------------------------------------------

class Bike(Vehicle):

    def __init__(self, brand, model, bike_type):
        # Call parent constructor
        super().__init__(brand, model)
        self.bike_type = bike_type

    def display_details(self):
        print("\n----- BIKE DETAILS -----")
        # Call parent method
        super().display_details()
        print("Bike Type:", self.bike_type)
# ------------------------------------------
# CREATING OBJECTS
# ------------------------------------------
car1 = Car("Toyota", "Fortuner", 5)
bike1 = Bike("Yamaha", "R15", "Sports")
# ------------------------------------------
# DISPLAYING DETAILS
# ------------------------------------------
car1.display_details()
bike1.display_details()
# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day 