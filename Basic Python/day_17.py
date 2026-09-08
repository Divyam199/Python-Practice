# Welocome Back !

# ==========================================
# INTRODUCTION TO OOP IN PYTHON
# ==========================================

# ------------------------------------------
# WHAT IS OOP?
# ------------------------------------------
# - OOP stands for Object-Oriented Programming.
# - It is a programming approach where we use
# - Classes and Objects to organize our code.

# Class  = Blueprint
# Object = Real instance created from a Class

# ------------------------------------------
# CREATING A SIMPLE CLASS
# ------------------------------------------

class Student:
    name = "Rahul"
    age = 18
# Creating an object
student1 = Student()
print("----- SIMPLE CLASS -----")
print("Name:", student1.name)
print("Age:", student1.age)
# Here student1 is the object which is used to access variables
# in the Class

# ------------------------------------------
# CREATING MULTIPLE OBJECTS
# ------------------------------------------

class Car:
    brand = "Toyota"

car1 = Car()
car2 = Car()
print("\n----- MULTIPLE OBJECTS -----")
print("Car 1 Brand:", car1.brand)
print("Car 2 Brand:", car2.brand)

# ------------------------------------------
# UNDERSTANDING SELF
# ------------------------------------------

class Person:

    def introduce(self):
        print("Hello! I am a person.")

person1 = Person()

print("\n----- SELF KEYWORD -----")
person1.introduce()

# self here points to the object which is being used in the class.

# So here person1 which is an object is being referred to as self
# inside the class Person

# Suppose you have multiple objects using the same class, there the self is 
# helping us differentiate between the two objects or we can say which object is 
# calling the function in the class.

# ------------------------------------------
# USING **init** CONSTRUCTOR
# ------------------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 18)

print("\n----- CONSTRUCTOR -----")
print("Name:", student1.name)
print("Age:", student1.age)


# ------------------------------------------
# INSTANCE VARIABLES
# ------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Amit", 30000)
employee2 = Employee("Priya", 40000)

print("\n----- INSTANCE VARIABLES -----")
print("Employee 1:", employee1.name)
print("Salary:", employee1.salary)
print()
print("Employee 2:", employee2.name)
print("Salary:", employee2.salary)

# Here the use of self can be understood clearly
# When employee1 is the object being used self denotes
# employee1 so for understanding we can say
# self.name here is equal to employee1.name, same process happens
# for employee2.

# ------------------------------------------
# INSTANCE METHODS
# ------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Rahul", 85)

print("\n----- INSTANCE METHOD -----")
student1.display()

# ------------------------------------------
# MODIFYING OBJECT ATTRIBUTES
# ------------------------------------------

class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mobile1 = Mobile("Samsung", 25000)

print("\n----- MODIFYING ATTRIBUTES -----")

print("Original Price:", mobile1.price)

# Changing object attribute

mobile1.price = 22000

print("New Price:", mobile1.price)

# ------------------------------------------
# MULTIPLE OBJECTS WITH DIFFERENT DATA
# ------------------------------------------

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

book1 = Book("Python Basics", "John")
book2 = Book("Learn Programming", "David")

print("\n----- BOOK DETAILS -----")

book1.display()

print()

book2.display()

# ==========================================
# ==========================================
# ==========================================
# CHALLENGE - Write a code to create a STUDENT MANAGEMENT SYSTEM.
# Requirements - 1. Create a class Students, it should:
                    # Store different students (Name, roll_number, marks)
                    # Display Details stored
                    # Calculate and return grade (A+(>90), A(>80), B(>70), 
                    #  C(>60), D(>40), F(<40))
                    # Display result as pass or fail
#                2. Create different objects which pass the students details and 
#                   call the functions of class


class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks


    # Display student details

    def display_details(self):
        print("\n----- STUDENT DETAILS -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


    # Calculate Grade

    def calculate_grade(self):

        if self.marks >= 90:
            return "A+"

        elif self.marks >= 80:
            return "A"

        elif self.marks >= 70:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "F"


    # Check Pass or Fail

    def check_result(self):

        if self.marks >= 40:
            return "PASS"

        else:
            return "FAIL"

# Creating Multiple Student Objects

student1 = Student("Rahul", 101, 85)
student2 = Student("Priya", 102, 92)
student3 = Student("Amit", 103, 35)

# Displaying Student 1

student1.display_details()

print("Grade:", student1.calculate_grade())
print("Result:", student1.check_result())

# Displaying Student 2

student2.display_details()

print("Grade:", student2.calculate_grade())
print("Result:", student2.check_result())

# Displaying Student 3

student3.display_details()

print("Grade:", student3.calculate_grade())
print("Result:", student3.check_result())

# ==========================================
# ==========================================
# ==========================================


# Have a Nice Day