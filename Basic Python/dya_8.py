#Welcome Back !

# =====================================================================
# Nested Loops in Python
# =====================================================================
# A nested loop is simply a loop inside another loop.Think of it like a clock: the outer loop is the hour hand, 
# and the inner loop is the minute hand. The hour hand moves forward by one tick only after the minute hand completes 
# a full rotation of 60 ticks.
# How it works:The outer loop starts its first iteration.The inner loop executes completely from start to finish.The 
# outer loop moves to its second iteration.The inner loop executes completely all over again.
# Simple Example:
# Outer loop runs 2 times
for row in range(1, 3):
    # Inner loop runs 3 times for EVERY outer loop turn
    for col in range(1, 4):
        print(f"Row {row}, Col {col}")
# -----------------------
# Output : Row 1, Col 1
#          Row 1, Col 2
#          Row 1, Col 3
#          Row 2, Col 1
#          Row 2, Col 2
#          Row 2, Col 3


# =====================================================================
# LOOP CONTROL PATTERNS
# DESCRIPTION: Generating visual shapes using string multiplication.
# =====================================================================

# ---------------------------------------------------------------------
# PATTERN 1: FULL PYRAMID
# Expected Output Shape (for n=4):
#      *
#     ***
#    *****
#   *******
# ---------------------------------------------------------------------
print("\n=== 1. FULL PYRAMID ===")
# Prompt the user specifically for the pyramid pattern size
n_pyramid = int(input("Enter the size for the Full Pyramid: "))

for i in range(1, n_pyramid + 1):
    # ' ' * (n_pyramid - i) creates the shifting alignment padding
    # '*' * (2 * i - 1) generates the odd number sequence of stars
    print(f"{' ' * (n_pyramid - i)}{'*' * (2 * i - 1)}")


# ---------------------------------------------------------------------
# PATTERN 2: DIAMOND SHAPE
# Expected Output Shape (for n=4):
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *
# ---------------------------------------------------------------------
print("\n=== 2. DIAMOND PATTERN ===")
# Prompt the user specifically for the diamond pattern size
n_diamond = int(input("Enter the size for the Diamond: "))

# The loop runs for (2 * n_diamond - 1) rows to cover top and bottom halves
for i in range(1, 2 * n_diamond):
    if i <= n_diamond:
        # Top half: identical math logic to the regular pyramid
        print(f"{' ' * (n_diamond - i)}{'*' * (2 * i - 1)}")
    else:
        # Bottom half: mirrors the calculations in reverse using (2*n_diamond - i)
        print(f"{' ' * (i - n_diamond)}{'*' * (2 * (2 * n_diamond - i) - 1)}")


# =====================================================================
# =====================================================================
# =====================================================================
# Write a code to generate a HOLLOW SQUARE
# Expected Output Shape (for n=4):
#   ****
#   *  *
#   *  *
#   ****
# ---------------------------------------------------------------------
# Prompt the user specifically for the hollow square size
n_square = int(input("Enter the size for the Hollow Square: "))

for i in range(1, n_square + 1):
    # Condition to print solid lines for the ceiling and floor borders
    if i == 1 or i == n_square:
        print(f"{'*' * n_square}")
    else:
        # Middle rows print a border star, inner spaces, and a trailing star
        # Inner hollow space count is always exactly (n_square - 2)
        print(f"*{' ' * (n_square - 2)}*")

# =====================================================================
# =====================================================================
# =====================================================================

# Have a Nice Day
