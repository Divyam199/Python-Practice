# Python - It is a progamming language which helps us in telling the Machine what operation 
#          it needs to perform (High Level Language ==> Low Level Language). It is the easiest   
#          programming language because its code almost like simple readable english.  
#          It executes code line by line with the help of interpreter.

# Comments - In python comments means those lines of code which is not executed by Python.
#          They are written by adding " # " before the text we want as comment. It is done so 
#          python knows it does not have to execute those line so it will not raise error even if it doesn't
#          understand it (Comments are being used to type the explanation).

# ==========================================
# First Python Code
# ==========================================
print("Hello World!")

# 1> **"print()"** - It is a function used to display the output. 
# 2> Functions - A function is a reusable block of code that only runs when we call it. So instead of 
#            writing multiple lines of code it make the programmers life easy. We can perform a complex 
#            by simply calling a function (like print) to get the result without worrying about the difficult
#            part.
# 3> "Hello World" - In python anything written inside double quotes or single quotes or triple quotes ("", '', """ """, ''' ''')
#            is considered to be a text (String Data-Type). So whatever we write inside the double quotes and 
#            give it inside the print the print function it will be displayed as it is in the output.
#            eg - print("github"), 
#                 print('CLoudy Day'), 
#                 print('+").

# ==========================================
#Data-Types - How Python stores Values (Containers which store value according to their properties).
# ==========================================

#                                                             ┌───────────────────┐
#                                                             │ Python Data Types │
#                                                             └─────────┬─────────┘
#                                                                       │
#                                                ┌──────────────────────┴──────────────────────┐
#                                                ▼                                             ▼
#                                        ┌───────────────┐                             ┌───────────────┐
#                                        │   Primitive   │                             │  Collection   │
#                                        │(Single Values)│                             │(Grouped Values)
#                                        └───────┬───────┘                             └───────┬───────┘
#                                                │                                             │
#                                        ┌───────┼───────┬───────┬───────┐             ┌───────┼───────┬───────┐
#                                        ▼       ▼       ▼       ▼       ▼             ▼       ▼       ▼       ▼
#                                       ┌───┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌───────┐     ┌────┐ ┌──────┐ ┌──────┐ ┌────┐
#                                       │int│ │float│ │str  │ │bool │ │complex│     │list│ │tuple │ │dict  │ │set │
#                                       └───┘ └─────┘ └─────┘ └─────┘ └───────┘     └────┘ └──────┘ └──────┘ └────┘
#                                         │      │       │       │        │           │       │        │       │
#                                        Whole Decimal  Text   True/    Real &     Ordered  Ordered Key-Value Unordered
#                                        Numbers Numbers  Chars  False  Imaginary  Mutable Immutable  Pairs   Unique


# ==========================================
# Primitive Data-Types - They are inbuilt in python and they only have a single meaning. 
# ==========================================

#Printing Primitive Data types
print(1, 1.1, "11", True, (4+9j))  #Anything inside quotes is considered a string in python
# print(Int, Float, String, Boolean, Complex)

# ==========================================
# Variables - They are containers in python which are used to store a value. They are also called as objects or identifiers.
# ==========================================

a = 11
# 1> **"a"** - Variable Name
# 2> **11** - The value stored
#                                                               Variable Name (Label)
#                                                                     ┌───┐
#                                                                     │ a │
#                                                                     └───┘
#                                                                       │
#                                                                       │  (Points to / Stores value)
#                                                                       ▼
#                                                               ┌───────────────┐
#                                                               │ Memory Box    │
#                                                               │               │
#                                                               │      11       │
#                                                               │               │
#                                                               └───────────────┘
#                                                              Integer Data Type
# Examples
f = 1.1
s = "Sunny Day"
b = True
# **Variable Names** = **Values having different Data-Types**

# ==========================================
# Asking for Value from a user
# ==========================================

nme = input("Enter your name in reverse order")
# Variable Name = input("Message to be displayed")
# 1> **nme** - Variable Name
# 2> **input()** - Like print this is a **funtion** which is used when we want the user to enter the value,
#         so when we run the code we have to give the value which will be given to the variable.
# 3> **"Enter your name in reverse order"** - This is the message which will be displayed when we run the code.
#         We can write any messsage here but remember it should be in quotes.

# ==========================================
# ==========================================
# ==========================================
# Write a code to ask the user to enter the date of the month when he is reading this then diplay it using print.
date = input("Enter today's Date : ")
print("date")
# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day.


















