# Welcome Back !

# ============================================================
#                    FILE HANDLING
# ============================================================

# ------------------------------------------------------------
# WHAT IS FILE HANDLING?
# ------------------------------------------------------------
# File handling means working with files using Python.
# Python can:
# - Create files
# - Read files
# - Write to files
# - Add content to files

# Common file types: .txt, .csv, .json

# ------------------------------------------------------------
# OPENING A FILE
# ------------------------------------------------------------
# open() is used to open a file.

# Syntax:
# open("filename", "mode")

# Common modes:

# "r" -> Read
# "w" -> Write
# "a" -> Append

# ------------------------------------------------------------
# READING A FILE
# ------------------------------------------------------------
# Suppose we have a file called "sample.txt"

# sample.txt:

# Hello Python!
# I am learning file handling.
file = open(".txt_files/sample.txt", "w")  # When we open a file in "w" mode it creates the file if it does not exist.
file.close()                          # Here the path for the file is folder_name/"name".txt. Remember the folder should exist.
                                      # We can also use any other file path present in the system or just write the name of the 
                                      # txt file and it will be created in the working directory.
file = open(".txt_files/sample.txt", "r")
content = file.read()
print(content)
file.close()


# ------------------------------------------------------------
# WHY DO WE CLOSE A FILE?
# ------------------------------------------------------------
# After working with a file, we should close it.

# file.close()

# This tells Python that we are finished working with the file.

# ------------------------------------------------------------
# USING "with open()"
# ------------------------------------------------------------
# A better way to work with files is using "with".
# Python automatically closes the file after the block finishes.

with open(".txt_files/sample.txt", "r") as file:
    content = file.read()

    print(content)

# ------------------------------------------------------------
# WRITING TO A FILE
# ------------------------------------------------------------
# "w" mode is used to write data into a file.
# IMPORTANT:
# "w" will overwrite existing content.

with open(".txt_files/sample.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Today I am learning File Handling.")

# ------------------------------------------------------------
# APPENDING TO A FILE
# ------------------------------------------------------------
# "a" mode adds new content at the end of the file.
# Existing content is NOT removed.

with open(".txt_files/sample.txt", "a") as file:
    file.write("\nThis line was added later.")

# ------------------------------------------------------------
# READING LINE BY LINE
# ------------------------------------------------------------

with open(".txt_files/sample.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline() #It automatically gives the next line every time
    print("\nFirst Line:")
    print(first_line)
    print("Second Line:")
    print(second_line)

# ------------------------------------------------------------
# READLINES()
# ------------------------------------------------------------
# readline()  -> reads one line
# readlines() -> reads all lines and returns a list

with open(".txt_files/sample.txt", "r") as file:
    lines = file.readlines()
    print("\nAll Lines:")
    print(lines)

# ------------------------------------------------------------
# LOOPING THROUGH A FILE
# ------------------------------------------------------------

with open(".txt_files/sample.txt", "r") as file:
    print("\nReading Line by Line:")
    for line in file:
        print(line.strip())  # **.strip()** - Removes the spaces if present in the start and end.

# ------------------------------------------------------------
# 11. SIMPLE FILE PROGRAM
# ------------------------------------------------------------
# Do not run this in command prompt
name = input("\nEnter your name: ")
age = input("Enter your age: ")
with open(".txt_files/user.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
print("\nYour information has been saved!")

# ------------------------------------------------------------
# READING THE SAVED INFORMATION
# ------------------------------------------------------------

with open(".txt_files/user.txt", "r") as file:
    information = file.read()
    print("\nSaved Information:")
    print(information)

# ============================================================
#                         KEY POINTS
# ============================================================

# open()       -> Opens a file
# "r"          -> Read
# "w"          -> Write / overwrite
# "a"          -> Append
# read()       -> Reads entire file
# readline()   -> Reads one line
# readlines()  -> Reads all lines
# write()      -> Writes content
# close()      -> Closes the file
# with open()  -> Safely works with files

# ============================================================
# ============================================================
# ============================================================
# Challange - Create a program that allows the user to:
#           1. Add a note
#           2. View all notes
#           3. Exit
# Store the notes inside a file called "notes.txt".
# Example:
#       1. Add Note
#       2. View Notes
#       3. Exit
# Enter your choice: 1
# Enter your note: Learn Python File Handling
# Note saved successfully!

def add_note():
    with open(".txt_files/notes.txt", "a") as file:
        wrt = input("Write Your Notes : \n")
        file.write(wrt+"\n")
    print("\nYour information has been saved!")

def view_note():
    with open(".txt_files/notes.txt", "r") as file:
        for line in file:
            print(line.strip())

while True:
    choice = int(input("1. Add Note\n2. View Note\n3. Exit\nEnter Your Choice :"))
    if choice==1:
        add_note()
    elif choice==2:
        view_note()
    else:
        break
    
# ============================================================
# ============================================================
# ============================================================

# Have a Nice Day