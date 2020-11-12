import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper and Scissors!")
user = int(input("Choose a move: Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if user>=3 or user<0:
    print("You typed an invalid number")
    exit()
moves = [rock,paper,scissors]
print(moves[user])
computer = random.randint(0,2)
print(f"The computer chose: {moves[computer]}")
# print(moves[computer])

if user == computer:
    print("It's a draw")
elif user == 0 and computer == 2:
    print("You win")
elif computer> user:
    print("You lose")
elif computer == 0 and user == 0:
    print("You lose")
elif computer < user:
    print("You win")

