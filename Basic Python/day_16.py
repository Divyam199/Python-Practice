# Welcome Back !

# ==========================================
# EXCEPTION HANDLING IN PYTHON
# ==========================================

# ------------------------------------------
# WHAT IS EXCEPTION HANDLING?
# ------------------------------------------
# An exception is an error that occurs while
# the program is running.

# ------------------------------------------
# BASIC TRY AND EXCEPT
# ------------------------------------------
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# ------------------------------------------
# ZERO DIVISION ERROR
# ------------------------------------------
try:
    number = int(input("\nEnter a number: "))
    result = 100 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error! You cannot divide by zero.")
except ValueError:
    print("Error! Please enter a valid number.")

# ------------------------------------------
# MULTIPLE EXCEPT BLOCKS
# ------------------------------------------
try:
    numbers = [10, 20, 30]
    index = int(input("\nEnter an index (0-2): "))
    print("Value:", numbers[index])
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index is out of range.")

# ------------------------------------------
# USING ELSE
# ------------------------------------------
try:
    age = int(input("\nEnter your age: "))

except ValueError:
    print("Invalid age!")
else:
    print("Your age is:", age)

# ------------------------------------------
# USING FINALLY
# ------------------------------------------

try:
    num = int(input("\nEnter a number: "))
    print("Result:", 100 / num)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program finished.")  

# ------------------------------------------
# FILE NOT FOUND ERROR
# ------------------------------------------
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")

# ------------------------------------------
# KEY ERROR
# ------------------------------------------
student = {
"name": "Rahul",
"age": 18
}
try:
    print(student["marks"])
except KeyError:
    print("This key does not exist.")

# ------------------------------------------
# RAISING AN EXCEPTION
# ------------------------------------------
try:
    age = int(input("\nEnter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)

except ValueError as error:
    print("Error:", error)

# ==========================================
# ==========================================
# ==========================================
# CHALLENGE - Create a SAFE ATM PROGRAM which :
                #1. Takes input from user of withdrawal amount
                #2. Raises error when withdrawal amount is 0.
                #3. If withdrawal amount > Balance print Insufficient Balance
                #4. If conditions are met print the remaining balance
                #5. Show invalid input for wrong input from user
                #6 And Finally print Thank you.

print("\n===== SAFE ATM PROGRAM =====")

balance = 5000
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")    
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
except ValueError as error:
    print("Invalid input:", error)
finally:
    print("Thank you for using the ATM!")
    print("Transaction completed.")
# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day