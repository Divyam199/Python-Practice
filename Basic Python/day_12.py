# Welcome Back !

# ============================================================
# FUNCTION PRACTICE
# ============================================================

# Function with no parameters
def say_hello():
    print("Hello from Day 12!")
say_hello()

# Function with one parameter
def square(number):
    return number ** 2
print("Square:", square(5))

# Function with multiple parameters
def add(a, b):
    return a + b
print("Sum:", add(10, 20))

# ============================================================
# COMMON FUNCTION-BASED PROBLEMS
# ============================================================

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

def find_largest_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

def factorial(number):
    if number < 0:
        return None
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def calculate_average(a, b, c):
    return (a + b + c) / 3

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for character in text.lower():
        if character in vowels:
            count += 1
    return count

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# ============================================================
# FUNCTIONS + COLLECTIONS
# ============================================================

def list_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def list_average(numbers):
    if len(numbers) == 0:
        return None
    return list_total(numbers) / len(numbers)  # Calling the lsist_total function to get the sum of elements

def list_highest(numbers):
    if len(numbers) == 0:
        return None
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

def list_lowest(numbers):
    if len(numbers) == 0:
        return None
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

def count_item(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

# Example
numbers = [10, 20, 30, 40, 50]

print("\nList:", numbers)
print("Total:", list_total(numbers))
print("Average:", list_average(numbers))
print("Highest:", list_highest(numbers))
print("Lowest:", list_lowest(numbers))


# ============================================================
# FUNCTIONS CALLING OTHER FUNCTIONS
# ============================================================

def calculate_total(marks):
    return list_total(marks)

def calculate_marks_average(marks):
    return list_average(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

marks_example = [85, 78, 92, 95, 81]

average_example = calculate_marks_average(marks_example)

print("\nExample marks:", marks_example)
print("Average:", average_example)
print("Grade:", calculate_grade(average_example))


# ============================================================
# MENU-DRIVEN PROGRAM
# ============================================================

def display_menu():
    print("\n===== Student Utility =====")
    print("1. Calculate Average")
    print("2. Check Grade")
    print("3. Find Highest Score")
    print("4. Find Lowest Score")
    print("5. Exit")


def get_marks():
    marks = []
    number_of_subjects = int(input("Enter number of subjects: "))
    for i in range(number_of_subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
    return marks

def student_utility():
    marks = get_marks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Average:", calculate_marks_average(marks))
        elif choice == "2":
            average = calculate_marks_average(marks)
            print("Grade:", calculate_grade(average))
        elif choice == "3":
            print("Highest:", list_highest(marks))
        elif choice == "4":
            print("Lowest:", list_lowest(marks))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Uncomment this line to run the menu-driven program.
#student_utility()

# ============================================================
# STUDENT MARKS ANALYZER
# ============================================================

def display_report(marks):
    total = calculate_total(marks)
    average = calculate_marks_average(marks)
    highest = list_highest(marks)
    lowest = list_lowest(marks)
    grade = calculate_grade(average)

    print("\n===== Student Marks Report =====")
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Grade:", grade)

# Example input
display_report([85, 78, 92, 95, 81])

# ============================================================
# ============================================================
# ============================================================
# Write a code to Create a function called check_subject_pass().

# Requirements:
# 1. Accept lists of marks and name.
# 2. Use 40 as the default passing mark.
# 3. Check every subject.
# 4. Identify subjects below the passing mark.
# 5. Display the subject name and mark for every failed subject.

def generate_report():
  num_sub = int(input("Enter the Number of Subjects :"))
  sub_mrk = {}
  for i in range(num_sub):
    name = input("Enter Subjec Name :")
    mrk = float(input("Enter Marks Scored :"))
    sub_mrk[name] = mrk
  marks = list(sub_mrk.values())
  names = list(sub_mrk.keys())
  return marks,names

def check_subject_pass(marks, names, passing_marks=40):
  fail = {}
  for i in range(len(marks)):
    if marks[i] < 40:
      fail[names[i]] = marks[i]
  print(f"Subjects Failed : {len(fail)}")
  for i in fail:
    print(f"{i} : {int(fail[i])}")

marks,names = generate_report()
check_subject_pass(marks,names)

# ============================================================
# ============================================================
# ============================================================


# Have a Nice Day
