print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size=="S":
    bill=15
    if pepperoni=="Y":
        bill=bill+2
    if extra_cheese=="Y":
        bill=bill+1
elif size=="M":
    bill=20
    if pepperoni=="Y":
        bill=bill+3
    if extra_cheese == "Y":
        bill = bill + 1
else:
    bill=25
    if pepperoni=="Y":
        bill=bill+3
    if extra_cheese == "Y":
            bill = bill + 1
print(f"Your final bill is: ${bill}.")