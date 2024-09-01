print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
split_bill = int(input("How many people to split the bill? "))

# Calculate the tip amount and add it to the total bill
# to convert a percentage to its decimal form (which you can use in calculations), you divide it by 100.
tip_amount = total_bill * (tip / 100)
final_bill = (total_bill + tip_amount) / split_bill

print(f"Each person should pay: ${final_bill: .2f}")
