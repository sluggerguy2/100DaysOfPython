import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

print("Welcome to my password generator!")
nr_letters = int(input("How many letters do you want? "))
nr_numbers = int(input("How many numbers do you want? "))
nr_symbols = int(input("How many symbols do you want? "))

for i in range(0, nr_letters):
    password += random.choice(letters)

for i in range(0, nr_numbers):
    password += random.choice(numbers)

for i in range(0, nr_symbols):
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)

shuffled_password = ""
for char in password_list:
    shuffled_password += char

print(f"Your password is {shuffled_password}")
