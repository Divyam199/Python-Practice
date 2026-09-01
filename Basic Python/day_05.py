#Welcome Back !


# ==========================================
# ==========================================
# ==========================================
# SOLUTION 1: WHOLE NUMBER BILL SPLITTER
# ==========================================
print("--- Question 1: Bill Splitter ---")
total_bill = float(input("Enter total bill amount: "))
people_count = int(input("Enter number of people splitting: "))

# Calculate raw split
share_amount = total_bill / people_count

# Cast to integer to drop decimals completely
final_share = int(share_amount)
print("Each person pays (rounded down): ₹" + str(final_share))


# ==========================================
# SOLUTION 2: SENIOR CITIZEN CHECKER
# ==========================================
print("\n--- Question 2: Senior Citizen Check ---")
birth_year = int(input("Enter your birth year: "))

# Calculate age based on the current year 2026
current_age = 2026 - birth_year

# Comparison operator outputs True or False automatically
is_senior = current_age >= 60
print("Is eligible for senior citizen discount: " + str(is_senior))


# ==========================================
# SOLUTION 3: DOMAIN EXTRACTOR FROM KEYS
# ==========================================
print("\n--- Question 3: Server Domain Lookup ---")
servers = {"US": "amazon.com", "IN": "flipkart.in"}

region_key = input("Enter region key (US/IN): ")

# Access the dictionary value via the direct key string
selected_domain = servers[region_key]
print("Target domain configuration set to: " + selected_domain)


# ==========================================
# SOLUTION 4: DYNAMIC LIST INDEXING
# ==========================================
print("\n--- Question 4: Lucky Draw Reward ---")
prizes = ["Bronze Ticket", "Silver Ticket", "Gold Ticket", "VIP Access Pass"]

user_number = int(input("Enter your lucky number: "))

# Using modulo (%) to wrap any number into a valid index (0, 1, 2, or 3)
calculated_index = user_number % 4

# Extract the single item using its position index
won_prize = prizes[calculated_index]
print("Congratulations! You have won a: " + won_prize)

# ==========================================
# ==========================================
# ==========================================


#Have a Nice Day
