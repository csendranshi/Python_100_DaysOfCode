print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L? ")
add_pep = input("Do you want to add pepperoni? Y or N? ")
add_cheese = input("Do you want to add extra cheese? Y or N? ")
amt=0
if size == 'S':
    amt+=15
    if add_pep=='Y':
        amt+=2

elif size == 'M':
    amt+=20
    if add_pep=='Y':
        amt+=3
else:
    amt+=25
    if add_pep=='Y':
        amt+=3

if add_cheese=='Y':
    amt+=1
print(f"You have to pay ${amt}")
