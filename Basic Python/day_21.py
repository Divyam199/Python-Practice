# Welcome Back

# ==========================================
# PYTHON PRACTICE PROBLEMS
# ==========================================


# ==========================================
# DUPLICATE ELEMENTS (Easy) 
# ==========================================
"""
Given a list of numbers, find all elements
that appear more than once.
Example:
[1, 2, 3, 2, 4, 5, 1, 6, 2]
Output:
[1, 2]
"""

def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return list(duplicates)

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 2]

print("----- DUPLICATES -----")
print("Original:", numbers)
print("Duplicates:", find_duplicates(numbers))

# ==========================================
# SECOND LARGEST NUMBER (Easy)
# ==========================================
"""
Find the second largest UNIQUE number.
Example:
[10, 5, 20, 8, 20, 15]
Output:
15
We will solve this without using sort().
"""

def second_largest(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    largest = None
    second_largest = None
    for number in unique_numbers:
        if largest is None or number > largest:
            second_largest = largest
            largest = number
        elif second_largest is None or number > second_largest:
            second_largest = number
    return second_largest

numbers = [10, 5, 20, 8, 20, 15]

print("\n----- SECOND LARGEST -----")
print("Numbers:", numbers)
result = second_largest(numbers)
if result is None:
    print("A second largest number does not exist.")
else:
    print("Second largest:", result)

# ==========================================
# WORD FREQUENCY ANALYZER (Medium)
# ==========================================
"""
Count how many times each word occurs
in a sentence.
Requirements:
* Ignore uppercase/lowercase differences.
* Remove basic punctuation.
* Store results in a dictionary.
* Display the most frequent word.
  """

def word_frequency(sentence):
    punctuation = ".,!?"
    # Convert everything to lowercase
    sentence = sentence.lower()
    # Remove punctuation
    for character in punctuation:
        sentence = sentence.replace(character, "")
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

print("\n----- WORD FREQUENCY -----")
sentence = input("Enter a sentence: ")
frequency = word_frequency(sentence)
print("\nWord frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

if max(frequency.values())>1:
    most_frequent = max(frequency, key=frequency.get)

    print("\nMost frequent word:", most_frequent)
    print("Frequency:", frequency[most_frequent])
elif max(frequency.values())==1:
    print("No repetetive words were entered.")
else:
    print("No words were entered.")

# ==========================================
# STUDENT MARKS ANALYZER (Medium)
# ==========================================
"""
Manage multiple students and their marks.
Tasks:
1. Calculate every student's average.
2. Determine PASS or FAIL.
3. Find highest average.
4. Find lowest average.
5. Display students above class average.
   """

students = {
"Rahul": [85, 72, 90],
"Aman": [65, 70, 68],
"Priya": [92, 95, 89],
"Neha": [35, 42, 38]
}

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_student_averages(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = calculate_average(marks)
    return averages

def find_highest_student(averages):
    return max(averages, key=averages.get)

def find_lowest_student(averages):
    return min(averages, key=averages.get)

def get_class_average(averages):
    return sum(averages.values()) / len(averages)

print("\n-----STUDENT ANALYZER -----")
averages = get_student_averages(students)
print("\nStudent Results:")
for name, average in averages.items():
    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"
print(
    name,
    "- Average:",
    round(average, 2),
    "-",
    result
)
highest_student = find_highest_student(averages)
lowest_student = find_lowest_student(averages)
class_average = get_class_average(averages)
print("\nHighest:", highest_student,
"-", round(averages[highest_student], 2))
print("Lowest:", lowest_student,
"-", round(averages[lowest_student], 2))
print("Class Average:", round(class_average, 2))
print("\nStudents above class average:")
for name, average in averages.items():
    if average > class_average:
        print(name)

# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day