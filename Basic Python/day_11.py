# Welcome Back !

# ============================================================
# 1. WHAT IS A FUNCTION?
# ============================================================
# A function is a reusable block of code that performs a task.
# We create a function using the `def` keyword.

# Syntax:
# def function_name():
#     # code

# We can execute the function by calling its name:
# function_name()

# A simple function example with no parameters
def greet():
    print("Hello! Welcome to Day 11 of Python.")
# Calling the function
greet()

# ============================================================
# 2. FUNCTION WITH PARAMETERS
# ============================================================
# Parameters allow us to pass information into a function.

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alex")
greet_user("Sam")

# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alex", 15)

# ============================================================
# 3. POSITIONAL ARGUMENTS
# ============================================================
# Arguments are matched with parameters according to their position.

def add_numbers(a, b):
    print(a + b)

add_numbers(10, 20)
add_numbers(50, 25)

# ============================================================
# 4. DEFAULT PARAMETERS
# ============================================================
# A default value is used when an argument is not provided.

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default("Taylor")
greet_with_default()

# ============================================================
# 5. RETURN STATEMENT
# ============================================================
# `return` sends a value back to the place where the function was called.
# `print()` displays a value.
# `return` gives a value back so that we can store or use it later.

def multiply(a, b):
    return a * b

result = multiply(6, 7)
print("Multiplication result:", result)
# We can also use the returned value directly.
print("Result:", multiply(8, 5))

# ============================================================
# 6. RETURNING MULTIPLE VALUES
# ============================================================
# A Python function can return more than one value.
# Python packs the values together, which can then be unpacked.

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

sum_result, difference = calculate(20, 8)
print("Sum:", sum_result)
print("Difference:", difference)

# ============================================================
# 7. VARIABLE SCOPE
# ============================================================
# A variable created inside a function is normally LOCAL to that function.
# It cannot normally be accessed outside the function.

def show_local_variable():
    message = "I am a local variable."  # Variable created inside function
    print(message)

show_local_variable()
# A variable created outside a function has GLOBAL scope.
course = "Python"


def show_course():
    print("Current course:", course)   # Using global varialble

show_course()

# ============================================================
# ============================================================
# ============================================================
# Write a function called `calculate_average()` that:
# 1. Accepts three numbers.
# 2. Calculates their average.
# 3. Returns the average.

def calculate_average(a, b, c):
  return (a+b+c)/3
  
print(calculate_average(10, 20, 30))
# ============================================================
# ============================================================
# ============================================================

# Have a Nice Day





