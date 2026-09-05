# Welcome Back !

# ============================================================
#              IMPORTING MODULES - PART 2
# ============================================================

from math import sqrt
print("Square Root:", sqrt(25))

# ============================================================
# IMPORTING MULTIPLE THINGS
# ============================================================
# We can import more than one thing from a module.

from math import sqrt, pi
print("\nMultiple Imports:")
print("Square Root:", sqrt(36))
print("PI:", pi)

# ============================================================
# IMPORT ALIAS
# ============================================================
# An alias is another name.
# We can give a module a shorter name.
# Example:
# import math as m
# Now we can use:
# m.sqrt()
# instead of:
# math.sqrt()

import math as m
print("\nUsing an Alias:")
print("Square Root:", m.sqrt(49))
print("PI:", m.pi)


# ============================================================
# THE random MODULE
# ============================================================
# Python also has a module called random.
# It is useful when we need random values.

import random

# ============================================================
# random.randint()
# ============================================================
# randint() gives us a random integer between two numbers.
# Example:
# random.randint(1, 10)
# gives a random number from 1 to 10.

number = random.randint(1, 10)
print("\nRandom Number:", number)

# ============================================================
# random.choice()
# ============================================================
# random.choice() chooses one random item from a list.

fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange"
]
fruit = random.choice(fruits)
print("Random Fruit:", fruit)

# ============================================================
# WHY IS random USEFUL?
# ============================================================
# random can be useful for:
# - Games
# - Random choices
# - Random numbers
# - Simple simulations

# ============================================================
# ============================================================
# ============================================================
# CHALLENGE - Create a simple random number game and Rock Paper Scissors Game.
# Your program should:
#     1. Create two functions (1. Number Game  2. Rock Paper Scissors) and give user the choice what
#        he wants to play.
#     2. For Number game - Generate a random number between 1 and 20. Store it in a variable.
#                        - Ask User to Enter a number between one and 20.
#                        - Display who wins.
#     4. For Rock Paper Scissors - Create a Dictionary of Rock, Paper, Scissors and use random.choice() to randomly 
#                          select one option.
#                        - Give the user an option to select one option. 
#                        - Display who wins.

print("\n=========================")
print("     MINI CHALLENGE")
print("=========================")

import random

def num_game():
    u_num = int(input("Enter a number between 1 and 20 : "))
    c_num = random.randint(1,20)
    print(f"Your Choice : {u_num} | Computer's Choice : {c_num}")
    if u_num > c_num:
        print("Congrats You Won !")
    elif u_num == c_num:
        print("Oh, It is a Draw")
    else :
        print("No, You Lost")

def rps_game():
    g_dict = {1:"Rock", 2:"Paper", 3:"Scissors"}
    c_wins = [1,-2] #Calculated by subtracting computer and user's choice to reduce the if statements.
                    #These are the only possibility when computer wins
    u_choice = int(input("1. Rock\n2. Paper\n3. Scissors\nEnter Your Choice : "))
    c_choice = random.choice(list(g_dict.keys()))

    if u_choice - c_choice == 0:
        print("Oh, It is a Draw !")
    elif c_choice - u_choice in c_wins :
        print("No, You Lost")
    else :
        print("Congrats You Won !")
    print(f"Your Choice : {g_dict[u_choice]} | Computer's Choice : {g_dict[c_choice]}")


while True:
    choice = int(input("1. Number Game\n2. Snake Water Gun\n3. Exit\nEnter Your Choice : "))
    if choice==3:
        break
    elif choice == 1:
        num_game()
    elif choice == 2:
        rps_game()
    else:
        print("Invalid Choice Choose Again")
    g = input("Want to Play Again (Y/N) : ").lower()
    if g=="n":
        break

# ============================================================
# ============================================================
# ============================================================


# Have a Nice day
