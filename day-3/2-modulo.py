a=6 % 2 #will be 0
print(a)
b=6 % 5 #will be 1
print(b)
c=6 % 4 #will be 2
print(c)
d=10 % 3 #will be 2
print(d)

gg=input("Put any number")

if int(gg)%2==0:
    print("Even")

else:
    print("Odd")

    #solution by Angela below


number_to_check = int(input("What is the number you want to check?"))

if number_to_check % 2 ==0:
    print("Even")

else:
    print("Odd")