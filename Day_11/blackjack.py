import random
logo = """ _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                       _/ |                
                      |__/                 """
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print("Hola BlackJack Gamer!")
run = True

while run:
    print(logo)
    rerun = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if rerun == 'n':
        run = False

    player_cards = random.choices(cards,k=2)
    player_total = sum(player_cards)
    print(f"\nYour cards: {player_cards}, current score {player_total}")
    computer_cards = random.choices(cards,k=2)
    computer_total = sum(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")
    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_card == 'y':
        player_cards.append(random.choice(cards))
        if 11 in player_cards and player_total > 21:
            player_cards.remove(11)
            player_cards.append(1)

        player_total = sum(player_cards)


    if sum(player_cards) == 21 and len(player_cards)==2:
        player_total=0
        print("-- Game Over --")
        exit()
    elif sum(computer_cards) == 21:
        computer_total=0
        print("-- Game Over --")
        exit()

    print(f"\nYour cards are: {player_cards}, with a total of {player_total}.")
    print(f"Computer's cards are: {computer_cards}, with a total of {computer_total}.")


    if player_total >= 21:
        print("-- Game Over --")
        exit()


    if computer_total > player_total:
        print("You lost.")
    elif computer_total < player_total:
        print("You won.")
    else:
        print("It's a draw.")