from art import logo,vs
from gamedata import data
import random

run = True
score=0
while run:
    print(logo)
    A = random.randint(0,len(data)-1)
    B = random.randint(0,len(data)-1)

    if A==B:
        continue
    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}.")

    print(vs)

    print(f"Compare B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}.")
    guess = input("\nWho has more followers? Type 'A' or 'B': ")
    if guess == 'A':
        guess = A
    else:
        guess = B
    compare = max(data[A]['follower_count'],data[B]['follower_count'])
    if int(data[guess]['follower_count']) == compare:
        score+=1
        print(f"You're right! Current score: {score}")

    else:
        print(f"That was incorrect, Game Over\nMax score: {score}.")
        exit()
