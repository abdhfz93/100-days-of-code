import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password1=""
# for _ in range(nr_letters):
#     test1=random.randint(0,51)
#     password1 += letters[test1]
#
# password2=""
# for _ in range(nr_numbers):
#     test2=random.randint(0,9)
#     password2 += numbers[test2]
#
# password3=""
# for _ in range(nr_symbols):
#     test3=random.randint(0,8)
#     password3 += symbols[test3]
#
# easy_password=password1+password2+password3
# print(easy_password)
# fp_list=list(easy_password)
# random.shuffle(fp_list)
# hard_password=''.join(fp_list)
# print(hard_password)
# password1=""
# for char in range(1,nr_letters+1):
#     random_char=random.choice(letters)
#     password1 +=random_char
# print(password1)
#
# password2=""
# for numb in range(1,nr_numbers+1):
#     random_numb=random.choice(numbers)
#     password2 +=random_numb
# print(password2)
#
# password3=""
# for symbl in range(1,nr_symbols+1):
#     random_symbl=random.choice(symbols)
#     password3 +=random_symbl
# print(password3)

password=""

for char in range (0, nr_letters):
    password+=random.choice(letters)

for char in range (0, nr_numbers):
    password+=random.choice(numbers)

for char in range (0, nr_symbols):
    password+=random.choice(symbols)


print(password)
final_password=list(password)
random.shuffle(final_password)
hard_password=""
for char in final_password:
    hard_password+=char

print(f"Your password is: {hard_password}")