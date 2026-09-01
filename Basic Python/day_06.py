# Welcome Back !

# ==========================================
# F-Strings (Formatted String Literals) - F-strings provide a fast, clean way to embed variables and 
# expressions inside string literals using a simple f prefix and {} curly braces.

# Basic f-string variable insertion
name = "Alice"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")

# F-string with expressions (math or methods)
price = 49.99
print(f"The total with a $5 discount is: ${price - 5}") 


# ==========================================
# Basic if and else Statements
# ==========================================
# Conditional statements control the execution flow. The code block inside an if statement runs only if 
# the condition evaluates to True. The else block runs if the condition is False.

# Checking if a user can vote
age = 19

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are too young to vote.")

# ==========================================
# The elif (Else-If) Ladder
# ==========================================
# Use elif when you need to check multiple, mutually exclusive conditions in sequence. 
# Python runs the block of the first condition that evaluates to True.

# Traffic light system
light_color = "Yellow"

if light_color == "Red":
    print("Stop!")
elif light_color == "Yellow":
    print("Slow down!")
elif light_color == "Green":
    print("Go!")
else:
    print("Invalid traffic light color.")

# ==========================================
# Nested if Statements
# ==========================================
#You can place an if statement inside another if statement to handle multi-layered or dependent conditions.

# Checking account status and balance
is_logged_in = True
balance = 150

if is_logged_in:
    if balance > 0:
        print(f"Welcome back! Your balance is ${balance}.")
    else:
        print("Welcome! Your account is empty.")
else:
    print("Please log in to view your balance.")


# ==========================================
# ==========================================
# ==========================================
# Write a code to ask for student name and score and print student name and grade based on th score entered 
# (>=90 = A, >=80 = B, >= 70 = C else F

# 1. Asking user for input
student_name = input("Enter student name: ")
score_input = input("Enter student score (0-100): ")

# 2. Type casting input safely
score = float(score_input)

# 3. Decision making via elif ladder
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# 4. Output results using f-strings
print(f"Result: {student_name} received a final grade of '{grade}' for their score of {score}.")

# ==========================================
# ==========================================
# ==========================================

# Have a Noce Day

