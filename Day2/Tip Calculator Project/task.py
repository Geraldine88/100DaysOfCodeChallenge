# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
#
#
print("********************************************* CARTHAN TIP CALCULATOR  **********************************************")
print("Welcome to the Tip Calculator")

# Getting bill
bill = float(input("What was the total bill: $"))
# print(f'${bill}')

# Choosing percentage of tip to be given
tip = int(input("How much tip (percentage) would you like to give? 10, 12 or 15: "))
#print(tip)

# How many people will share the bill
share_bill = int(input("How many people to split the bill? "))
#print(share_bill)

# tip/100 * bill + bill
calculate_tip = (((bill * tip) / 100) + bill ) / share_bill
calculate_tip = round(calculate_tip, 2)
print(f'Each person should pay: ${calculate_tip}')