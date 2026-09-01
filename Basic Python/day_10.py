# Welcome Back !

# ==========================================
# Indexing and Slicing Deep Dive
# ==========================================

print("--- 1. Positive & Negative Indexing ---")
text = "PYTHON"
# Positive:  P(0), Y(1), T(2), H(3), O(4), N(5)
# Negative: P(-6), Y(-5), T(-4), H(-3), O(-2), N(-1)

print(f"First character (Positive Index 0): {text[0]}")
print(f"Last character (Negative Index -1): {text[-1]}")
print(f"Third character from end (-3): {text[-3]}\n")


print("--- 2. Basic Slicing [start:stop] ---")
# Remember: start index is inclusive, stop index is exclusive
sample_list = [10, 20, 30, 40, 50, 60]

print(f"Original List: {sample_list}")
print(f"Slice [1:4]: {sample_list[1:4]}")      # Elements at index 1, 2, 3
print(f"Slice from start [:3]: {sample_list[:3]}") # First 3 elements
print(f"Slice to end [3:]: {sample_list[3:]}")     # From index 3 to the end
print(f"Negative slice [-3:-1]: {sample_list[-3:-1]}\n") # Relative to end


print("--- 3. Advanced Slicing [start:stop:step] ---")
numbers = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Numbers List: {numbers}")
print(f"Every second element [::2]: {numbers[::2]}")
print(f"Elements from index 1 to 8 with step 3 [1:8:3]: {numbers[1:8:3]}")
print(f"Reversed sequence [::-1]: {numbers[::-1]}\n")


print("--- 4. Slice Assignment (Mutable Types Only) ---")
mutable_list = ['a', 'b', 'c', 'd', 'e']
print(f"Before assignment: {mutable_list}")
mutable_list[1:4] = ['X', 'Y'] # Replaces 'b', 'c', 'd' with 'X', 'Y'
print(f"After assignment:  {mutable_list}\n")


print("--- 5. Out-of-Bounds Handling ---")
# Individual indexing out-of-bounds throws an IndexError:
# print(text[100]) -> Throws Error

# Slicing handles out-of-bounds gracefully without crashing: (Gives empty string, list etc)
print(f"Out-of-bounds slice text[:100]: '{text[:100]}'")
print(f"Empty slice due to bounds [50:100]: {numbers[50:100]}\n")

# ==========================================
# ==========================================
# ==========================================
# Write a code to create a Palindrome Checker
user_input = input("Enter a word or phrase to check: ")

# Clean the input: remove spaces and convert to lowercase
cleaned_input = user_input.replace(" ", "").lower()

# Reverse using slicing
reversed_input = cleaned_input[::-1]

if cleaned_input == reversed_input:
    print(f"✨ Success! '{user_input}' is a palindrome.")
else:
    print(f"❌ '{user_input}' is not a palindrome.")

# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day
