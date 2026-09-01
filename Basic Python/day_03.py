#Welcome Back!

# ==========================================
# Python Operators
# ==========================================
# - Operators tell Python which operations should be performed on values.
# - They are of 5 types :
#          1. Arithmetic - "+", "-", "*", Integer Division (Returns only the Integer Part) - "//,
#                          Modulus (Returns the remainder value) - "%"Power - "**"
                          print(10//3)    # Output ==> 3 
                          print(10%3)     # Output ==> 1
                          print(8**(1/3)) # Output ==> 2.0
#                          PEMDAS - Arithmetic operations follow this order.
#                                   1. Paranthesis
#                                   2. Exponent
#                                   3. Multiplication - Both multiplication and Division are on the same level 
#                                                 so while solving it solves from left to right.
#                                   3. Division - All divisions are included ("/", "//", "%")
#                                   4. Addition - Both Addition and subtraction are on the same level so they 
#                                                 follow the left to right solving rule.
#                                   4. Subtraction
#          2. Assignment - It is of 2 types:
#                                   1. Basic Assignment - "="
#                                   2. Compound Operators (Arithmetic + Basic Assignment Operators) - "+=", "-=" etc.
                          a = 10
                          a += 10
                          print(a) # Output ==> 20
#          3. Comparison - It is used to compare 2 or more compatible values and can return two outcome, either True or False.
#                        - They are of 6 types -
#                                   1. Equal to : **"=="**
#                                   2. Not Equal to : **"!="**
#                                   3. Greater than : **">"**
#                                   4. Less tahn : **"<"**
#                                   5. Greater than Equal to : **">="**
#                                   6. Less than Equal to : **"<="**
                          salary = int(input("Enter Salary = "))
                          print(10000 <= salary <= 50000)     # Checking whether salary is between 10K and 50K 
#          4. Logical - Logical operators combine multiple conditions into one condition.
#                     - It is used to overcome the limitation of comaparison 
#                       operators (When we have to check more than 2 conditions).
#                     - The output of logical operators will also either be True or False.
#                     - They are of three types -
#                                   1. and - It returns True only when all conditions return True
#                                   2. or - It returns True even if a single condition returns True.
#                                   3. not - It returns the reverse of the result.
                          print(salary >= 10000 and salary <= 50000) #Checking salary using AND
                          # Write a program to check whether the input given by user is january february or march
                          m = input("Enter Month Name")
                          m = m.lower() # this function converts all letters to lowercase
                          print(m == "january" or m == "february" or m == "march")
#          5. Membership - It is used to check whether the value is present or absent in a collection data type (eg - List).
#                        - They are of two types :
#                                    1. **"in"** - It is used to check the presence.
#                                    2. **"not in"** - It is used to check the absence.
#                                    3. Output is either True or False.
                          num = int(input("Enter the number : ")) # Checking presence of the number in the list
                          print(num in [1, 5, 7, 11, 15])
                          num = int(input("Enter the number : ")) # Checking absence of number in the list
                          print(num not in [1, 5, 7, 11, 15])
# - There are 2 more additional operators.
#          1. Identity Operators
#          2. Bitwise Operators

# ==========================================
# ==========================================
# ==========================================
#  Write a program that takes a three-digit integer from a user and sums its digits using arithmetic operators (// and %).
a = int(input("Enter a three digit number : ")) #Getting the input from user and type cast it to integer
a1 = a // 100                                   #Getting the first digit and assigning it to a1
a = a % 100                                     #Removing the first digit from the number
a2 = a // 10                                    #Getting the second digit which is now the first because we removed the digit on hundred place value
                                                #   and assigning it to a2
a = a % 10                                      #Removing the second digit 
a3 = a                                          #Getting the third digit and assigning it to a3
print(a1 + a2 + a3)                             #Adding the 3 digits
# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day
