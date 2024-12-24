print("Welcome to the tip calculator!")
bill_amount = input("What was the total bill? ")
total_bill = float(bill_amount[1:])
tip_amount = int(input("How much tip would you like to give? 10, 12 or 15? "))
split_count = int(input("How many people to split the bill?"))

# Calculation
tip_amount = tip_amount/100 * total_bill
payable_amount = (total_bill + tip_amount)/split_count

print(f"Each person should pay: ${payable_amount:.2f}")