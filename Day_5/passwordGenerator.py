#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy = ""
passwprd_len = nr_letters+nr_numbers+nr_symbols
for i in range(0, nr_letters):
    easy+=(random.choice(letters))

for i in range(0, nr_symbols):
    easy+=(random.choice(symbols))

for i in range(0, nr_numbers):
    easy+=(random.choice(numbers))

print("Your password is: ",easy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard =[]

for i in range(0, nr_letters):
    hard.append(random.choice(letters))

for i in range(0, nr_symbols):
    hard.append(random.choice(symbols))

for i in range(0, nr_numbers):
    hard.append(random.choice(numbers))
print("Before shuffle: ",hard)
random.shuffle(hard)

print("Your Password is: ","".join(hard))