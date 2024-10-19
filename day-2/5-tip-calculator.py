print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))
bill_w_tip=(bill*tip/100)+bill
after_split=bill_w_tip/people
final_amt=round(after_split,2)

print(f"Each person should pay: ${final_amt}")



