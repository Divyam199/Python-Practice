# Welcome Back !


# ==========================================
# Collection Data Types -
# ==========================================
# - Further divided into two types :
#            1. Sequence - Ordered, Indexed
#                        - Indexing means to use the position (index) number of the value present in the sequence data type.
#                        - Indexing always starts from 0 and goes till the total length -1 of that sequence data types.
#                        - Note : Don't get confused between len() and indexing, length always starts from 1 whereas indexing always starts from 0.
                         l = ["apple", "mango", "banana", "grapes", "orange", "pineapple", "strawberry"]
                         print(l[5])   # Output ==> "pineapple"  
#            2. Non Sequence - Unordered, Key-based
#                        - Dictionary does not supports index based extraction.
#                        - It supports key based extraction where key is the name of the key stored in the dictionary.
#                        - Sets do not support key based or index based extraction because it is an unordered collection of values.
                         x = {"Name" : "Mango", "Age" : 26, "Salary" : 1000}
                         #print(x[0])     #Gives error because cant call non-sequence based on index so we use keys
                         print(x["Name"])  # Output ==> "Mango"


# ==========================================
# Joining two Strings
# ==========================================
# - To perform a concatenate operation between strings (joining two strings) we can use "+" operator.
name = input("Enter your name : ")
print("Hello" + " " + name)
# - We get the output as Hello "__name_you_type__"
# - The **" "** part in the print statement adds a whitespace between Hello and the Name typed by user. We can add 
#   as many strings we want like this


# ==========================================
# **eval()** 
# ==========================================
# - This function solves an expression which is present in the form of strings.
# - So for example if we write "6 + 9", Normally it is considered as string in python brcause
#   it is inside double quotes, but if we pass the same string to **eval()** function it 
#   it does not treat it as a string and performs addition for 6 and 9 and we get 15.


# ==========================================
# ==========================================
# ==========================================
# Write a code to create a dynamic calculator and ask user to type the operation to perform on the two numbers.
num_1, num_2 = input("Enter No. 1 : "), input("Enter No. 2 : ")
operation = input("Enter a operation (+, -, *, /) : ")
print(eval(num_1 + operation + num_2)) # Output ==> The input has to be string so we can create an expression therefore
                                       #            we are joining them with "+" operator and passing it to the eval() funtion.
# ==========================================
# ==========================================
# ==========================================
