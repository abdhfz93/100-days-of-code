print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Still kid, so its $5.")
    elif age <= 18:
        bill=7
        print("Teen have price $7.")
    else:
        bill=12
        print("Still want go rollercoaster? Pay $12.")

    photos=input("want photo? y or n...")
    if photos=="y":
        bill+=3

    print(f"Ur final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
