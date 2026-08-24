# Welcome Back 

# ==========================================
# Rules For Naming a Variable
# ==========================================
# 1. Values of a variable can be changed.
# 2. Should not start with Special Characters or Numbers (Must start with letter or underscore).
# 3. They are case sensitive.
# 4. Can't use reserved keywords. Should not use functions as variable name.

# ==========================================
# Assignment of Multiple Values in a Single Line
# ==========================================

# First Method (Many to Many)
x, y, z = 10, 11 ,12 # x = 10   |   # y = 11    |   # z = 12
print(x, y, z)  # Output : 10, 11, 12

# Second Method (Single to Many)
x = y = z = 0   # All the variables x, y, z get the same value as 0
print(x, y, z)  # Output : 0, 0, 0

# ==========================================
# Collection Data-Types
# ==========================================
# It allows us to Store multiple values in a single variable/object.
# There are 4 types of collection data types:
#           1. Lists
#           2. Tuple
#           3. Dictionaries
#           4. Set
# 1. Lists - List is a collection data type which can store multiple values in an order.
#           - List are created in python using square brackets ([]) and values are seperated by comma.
#           - We can store different data types in a single list.
#           - It is **Ordered**, **Mutable** - values inside it can be changed, **Duplicates allowed**
#             example - list_1 = [1, 2, 3, 4, "hello there"]
# 2. Tuples - Tuple is similar to list the main difference between them is that tuples is **unchangeable**.
#           - Tuples are created in python using brackets (paranthesis) and values are seperatede by a comma.
#           - Note: If we dont use brackets but seperate the values by comma the also tuple is created.
#           - Comma is mandatory to use for tuple creation except for empty tuple (it differentiates the tuple from complex numbers (3 + 4j)). 
#           - It is **Ordered**, **Immutable** - values inside it cannot be changed, **Duplicates allowed** 
#             example - e = (10, 34.45, True)   
# 3. Sets - Sets are a collection of **unique values**.
#           - If we create sets with duplicate values it will store it only once .
#           - Sets in python are created using curly braces '{}' and values are seperated by a comma.
#           - To create empty sets we can not use curly braces because python identifies it as an empty Dictionary, we can make an emty set using set().
#           - It is an unordered collection of data type, It does not allows duplicates.
#             example - z = {1, 1, 1, True}  # True is exactly equal to 1 
#                   ==> print(z) ===> Output will be 1 because it does not allow duplicates.
# 4. Dictionaries - It is a collection of values stored in a Key : Value format.
#           - Dictionaries are created using curly braces "{}" similar to set and are seperated by commas.
#           - It is a non sequence data type.
#           - Keys should always be **unique** (Values can have duplicates), if duplicae key : values are given, the second key : value pair is stored.
#           - It is a non sequence data types because even though it is ordered it has most of the properties of non sequence data types.
#             example - z = {"dd" : 11, "aa" : "jjj"}


# ==========================================
# Type Casting / Type Conversion
# ==========================================
# - It means to convert one data type value into another data type value.
# - But note there are some rules for type conversion which we need to follow else type casting will result in error.
# - It is of 2 types:
#           1. Implicit Type Casting - Python does it automatically (Dynamically Typed).
#           2. Explicit Type Casting - We as a user tell python to use a specific data type for the value provided.
# - We can use the built in functions for Explicit Type Casting:
#           1. int() - Converting any suitable value to Integer.
#           2. float() - Converting any suitable value to Float.
#           3. str() - Converting any suitable value to String.
#           4. bool() - Converting any suitable value to Boolean.
#           5. list() - Converting any suitable value to List.
#           6. tuple() - Converting any suitable value to Tuple.
#           7. set() - Converting any suitable value to Set.
#           8. dict() - Converting any suitable value to Dictionary.
# #### Common Errors during Type Casting
# 1. ValueError - It occurs when you try to convert a value into another data type which is not possible for python.
# 2. TypeError - It occurs when we tryb to perform an operation between teo different data type values which is noot possible for python.

# ==========================================
# ==========================================
# ==========================================
# Write a code to ask user for values for 2 variables (x, y)
# and swap there values. Output should show x = 20 and y = 10

# Method 1 (Without Temporary variable)
x = int(input("Enter value for 1st variable : ")  #Type Casting is being performed to convert the output to integer
y = int(input("Enter value for 2nd variable : ")  #Type Casting is being performed to convert the output to integer
x, y = y, x #Many to Many used instead of a temporary variable.
print(x,y)

# Method 2 (Using a Temporary Variable)
x = int(input("Enter value for 1st variable : ")  #Type Casting is being performed to convert the output to integer
y = int(input("Enter value for 2nd variable : ")  #Type Casting is being performed to convert the output to integer
temp = x #temporary variable to hold x value while x is changed to y.
x = y 
y = temp
print(x,y)
# ==========================================
# ==========================================
# ==========================================

#Have a Nice Day.

