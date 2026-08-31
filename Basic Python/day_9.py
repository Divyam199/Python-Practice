# Welcome Back

# ==========================================
# Collection Data Types Deep Dive
# ==========================================

# 1. LISTS (Ordered & Mutable)
print("--- 1. Lists ---")
fruits = ["apple", "banana"]

# Modifying lists
fruits.append("cherry")      # Adds to the end
fruits.insert(1, "orange")   # Inserts at index 1
fruits.extend(["mango", "grape"]) # Merges another list
print("After additions:", fruits)

# Removing items
popped_item = fruits.pop()   # Removes and returns last item, We can also pass the index inside pop to remove specific data
fruits.remove("banana")      # Removes specific item
print(f"Popped: {popped_item} | Remaining: {fruits}")

# Sorting
fruits.sort()                # Alphabetical sort (Ascending Order)
print("Sorted list:", fruits)
fruits.sort(reverse=True)    # (Descending Order)
print("Sorted list:", fruits)


# 2. TUPLES (Ordered & Immutable)
print("\n--- 2. Tuples ---")
coordinates = (10, 20, 30)
print("Original Tuple:", coordinates)

# Tuples cannot be changed: coordinates[0] = 50 -> Throws TypeError

# Tuple Unpacking
x, y, z = coordinates
print(f"Unpacked variables -> x: {x}, y: {y}, z: {z}")


# 3. DICTIONARIES (Key-Value Pairs)
print("\n--- 3. Dictionaries ---")
student = {
    "name": "Alex",
    "age": 21,
    "course": "Python"
}

# Safe accessing using .get()
print("Course:", student.get("course"))
print("Grade (Not found):", student.get("grade", "Not Assigned"))

# Extracting components
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items (Pairs):", list(student.items()))


# 4. SETS (Unordered & Unique)
print("\n--- 4. Sets ---")
# Eliminating duplicates automatically
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Original List:", numbers)
print("Unique Set:", unique_numbers)

# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union (All):", set_a.union(set_b))
print("Intersection (Common):", set_a.intersection(set_b))

# ==========================================
# ==========================================
# ==========================================
# Write a code to create a Student Database Management System

# Database structural setup
student_records = {}
num_stu = int(input("how many students you want to add :"))
roll_numbers = set(range(1,num_stu + 1))  # Set for unique IDs
for i in range(num_stu):
    stud = {}
    name = input(f"Enter Student {i+1} Name :")
    stud["name"] = name
    sub = []
    for j in range(2):
        s = input(f"Enter Subject {j+1} :")
        sub.append(s)
    stud["subjects"] = tuple(sub)
    student_records[i+1] = stud

# User Interactive Lookup
search_id = int(input("Enter Roll Number to lookup (e.g., 1, 2): "))

if search_id in roll_numbers and search_id in student_records:
    record = student_records[search_id]
    print(f"\n[Match Found]\nName: {record['name']}\nSubjects: {', '.join(record['subjects'])}")
else:
    print("\nError: Record does not exist in our database.")
# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day






