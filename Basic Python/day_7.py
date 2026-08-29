# Welcome back !

# ==========================================
# Introduction to Loops
# ==========================================
# Loops allow us to execute a block of code multiple times. 
# They prevent code repetition (DRY Principle: Don't Repeat Yourself).
# Each pass through a loop is called an "iteration".

# ==========================================
# The while Loop
# ==========================================
# A while loop repeats as long as a specified condition remains True.
# CRITICAL: Always ensure the condition eventually becomes False, 
# otherwise you will create an "infinite loop" that crashes your program.

print("--- 2. While Loop Example ---")
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1  # Crucial update step to avoid infinite loop
print("Blast off!\n")


# ==========================================
# The for Loop
# ==========================================
# A for loop is used to iterate over a sequence (like a string, list, or range).
# It automatically moves to the next item and terminates when the sequence ends.

print("--- 3. For Loop Example ---")
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"I like {fruit}")


# ==========================================
# The range() Function
# ==========================================
# range() generates a sequence of numbers. It is highly optimized for loops.
# Syntax: range(start, stop, step)
# Note: The 'stop' value is always exclusive (not included in the sequence).

print("--- 4. Range Function Examples ---")
# Example A: range(stop) -> starts at 0, increments by 1
for i in range(3):
    print(f"Count: {i}")  # Output: 0, 1, 2

# Example B: range(start, stop, step)
for num in range(10, 40, 10):
    print(f"Step Count: {num}")  # Output: 10, 20, 30


# ==========================================
# Loop Control Statements
# ==========================================
# These statements alter the normal execution flow of a loop.
# break: Exits the loop entirely.
# continue: Skips the rest of the current iteration and jumps to the next one.

print("--- 5. Loop Control Statements ---")
# **Continue**
for n in range(1, 6):
    if n == 3:
        continue  # Skips printing 3
    print(n)


# **break**
for n in range(1, 6):
    if n == 4:
        break  # Stops the loop entirely
    print(n)


# ==========================================
# ==========================================
# ==========================================
# Challenge: Multiplication Table Generator

# Challenge Statement: Ask the user for a number and print its 
# multiplication table (1 to 10) using a for loop.

user_num = int(input("Enter an integer to get its multiplication table: "))
print(f"\nMultiplication Table for {user_num}:")
    
# range(1, 11) generates numbers from 1 up to 10
for i in range(1, 11):
    product = user_num * i
    print(f"{user_num} x {i} = {product}")
        
# ==========================================
# ==========================================
# ==========================================
