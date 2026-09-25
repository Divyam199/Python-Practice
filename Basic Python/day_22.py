# Welcome Back

# ==========================================
# PYTHON PRACTICE PROBLEMS
# ==========================================

# ==========================================
# Write a code to check whether given year is Leap Year
# ==========================================

# Method 1

year = int(input("Enter Year : "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print("Yes Leap Year")
else:
    print("Not a Leap Year")

# Method 2

import calendar

calendar.isleap(year) # Using Library

# ==========================================
# Calculate Electricity Bill by breaking units
# For <100 charge 2 Rs, >100 and <300 charge 4 Rs, >300 charge 6 Rs then calculate the bill
# ==========================================

a = int(input("Enter the units : "))

if a<=100:
    print("Bill : Rs",a*2)
elif a>100 and a<=300:
    print("Bill : Rs",100*2+(a-100)*4)
else:
    print("Bill : Rs",100*2+(200)*4+(a-300)*6)

# ==========================================
# ==========================================
# ==========================================

# Have a Nice Day
