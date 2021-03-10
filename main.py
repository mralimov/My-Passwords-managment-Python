# Password Generator Project
import random
from password_symbols import letters
from password_symbols import symbols
from password_symbols import numbers
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
new_password = ""
for letter in range(1, nr_letters + 1):
    random_letter_choice = random.choice(letters)
    password += random_letter_choice


for number in range(1, nr_numbers + 1):
    random_number_choice = random.choice(numbers)
    password += random_number_choice


for symbol in range(1, nr_symbols + 1):
    random_symbol_choice = random.choice(symbols)
    password += random_symbol_choice


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)


for el in password:
    new_password += el

print(new_password)
