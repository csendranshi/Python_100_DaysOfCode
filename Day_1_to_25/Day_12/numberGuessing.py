import random

my_number = random.randint(1,100)

print("Welcome to the number Guessing Game\n I am thinking of an Integer number between 1 and 100")
level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if level == 'easy':
    lives_remaining = 11
elif level == 'hard':
    lives_remaining = 6

while lives_remaining > 0:
    print(f"You now have {lives_remaining-1} attempts to guess the number")
    guess = int(input("Make a guess: "))
    if guess == my_number:
        print("You've guessed the number.")
    elif guess > my_number:
        print("Too High.\nGuess again")
    elif guess < my_number:
        print("Too Low.\nGuess again")
    lives_remaining-=1

if lives_remaining==0:
    print("-- Game Over --")