# import random
#
# sentence ="this was the biggest disappointment of our trip. the restaurant had received some very good reviews, so our expectations were high. the service was slow even though the restaurant was not very full. I had the house salad which could have come out of any sizzler in the us. the keshi yena, although tasty reminded me of barbequed pulled chicken. this restaurant is very overrated"
# words = [word for word in list(map(str,sentence.split()))] #if word not in words]
# distinct_words = ['Jordan','Anshika']
# for i in range (len(words)):
#     if words[i] not in distinct_words:
#         distinct_words.append(words[i].strip('.'))
# print(distinct_words,len(distinct_words))
#
# print(" ".join(random.choices(distinct_words,k=30)))

import random, sys, time
from getkey import getkey
import sqlite3

conn = sqlite3.connect('score.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS HighScore(Name TEXT, Score REAL) ")


def insert_table(x, y):
    c.execute("INSERT INTO Highscore Values (?,?)", (x, y))
    conn.commit()
    c.close()
    conn.close()


# colours
blue = "\033[1;34m"
red = "\033[1;91m"
green = "\033[1;32m"
boot = "\033[0m"
shade = "\033[2m"
underline = "\033[4m"

# just all of the different passages
passages = [
    "Into the suitcase, I carelessly threw a pair of ripped jeans, my favorite sweater from high school, an old pair of tube socks with stripes, and $20,000 in cash.",

    "It can take a photon 40,000 years to travel from the core of the sun to the surface, but only 8 minutes to travel the rest of the way to earth.",

    "It would take 1,200,000 mosquitoes, each sucking once, to completely drain the average human of blood.",

    "A small percentage of the static you see on dead tv stations is left over radiation from the Big Bang. You're seeing residual effects of the Universe's creation.",

    "Written language was invented independently by the Egyptians, Sumerians, Chinese, and Mayans.",

    "If you were to remove all of the empty space from the atoms that make up every human on earth, the entire world population could fit into an apple.",

    "If you somehow found a way to extract all of the gold from the bubbling core of our lovely little planet, you would be able to cover all of the land in a layer of gold up to your knees.",

    "To know when to mate, a male giraffe will continuously headbutt the female in the bladder until she urinates. The male then tastes the pee and that helps it determine whether the female is ovulating.",

    "Crows can very easily distinguish humans apart from each other, whereas humans find it nearly impossible to tell crows apart",

    "The last naturally occurring case of smallpox was diagnosed in October 1977, and the last case of rinderpest was diagnosed in 2001.",

    "Kangaroos use their tails for balance whilst hopping, so if you elevate their tail, they would have no balance and fall over."

    "Bananas go through a process called “negative geotropism.” Instead of growing towards the ground, they start growing towards the sun"

    "An average human produces between 1 to 2 liters of saliva each day, which is a maximum of 730 liters per year"

    "Sea exploration and mapping didn’t truly start until the 1960s due to the lack of technology beforehand."

    "Saint Lucia was discovered by the French after they were shipwrecked on the island they arrived on December 13th which is the feast day of Saint Lucy – hence, why they named it Saint Lucia!"

    "The average person has the chance to recycle 25,000 cans in their lifetime – that’s 75,000 hours of television"

    "MTV may not have the most wholesome programs, but after the premier of this show, teen pregnancy dropped by 5.7% within 18 months of the show airing"

    "If you consider how large a blue whale’s heart is the size of a small car, it’s no surprise that a small child, around 3-4 years old, could swim through the massive veins of a blue whale."

    "In the popular sitcom, Parks and Recreation, the writers had no idea Nick Offerman was a talented saxophone player when they wrote the Duke Silver plot line."

    "Mike Tyson once offered a zoo attendant 10,000 dollars to let him fight a gorilla ,the zoo attendant said no."

    "In 2000, ABBA was offered $1 billion dollars to reunite for 100 shows – which would have been $250 million per member they turned it down because it wasn’t for them"

    "Queen Elizabeth II visited the set of Game of Thrones, but because of an obscure rule, she wasn’t allowed to sit on it – the ruling monarch can’t sit on a foreign throne, even if it’s fictional, apparently."

    "In 1990, the Prime Minister of New Zealand appointed Ian Brackenbury Channell, who was an old friend, as the Wizard of New Zealand. He is even given an annual stipend"

    "The average person walks the equivalent of five times around the world in their lifetime."

    "In an effort to extend his chocolate rations during World War Two, an Italian pastry maker mixed hazelnuts into chocolate ,the final Nutella product was created by his son who decided to perfect the recipe"

    "Ants leave pheromone trails when they walk as maps for other ants to follow, meaning they can travel the fastest route to food or their hive"

    "On average, male cats have a tail of 11 inches, whereas female cats have a tail of roughly 9.9 inches on average."

    "Dolly Parton entered a Dolly Parton themed drag queen contest, did her hair and makeup more dramatically, and not only lost, but received the least applause."

    "Four people lived in a home for 6 months infested with about 2,000 brown recluse spiders, but none of them were harmed."

    "Samuel L. Jackson requested a purple lightsaber in Star Wars in order for him to accept the part as Mace Windu."

    "The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair."

    "The tallest man ever recorded was American giant Robert Wadlow (1918–1940), who stood 8 feet 11 inches. Wadlow’s size was the result of abnormally enlarged pituitary gland"

    "The tallest living man is 37-year-old Sultan Kosen, from Turkey, who is 8 feet, 2.8 inches, who set the record in 2009. His growth is also due to a pituitary issue."

    "The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997"

    "The Earl of Sandwich, John Montagu, who lived in the 1700s, reportedly invented the sandwich so he wouldn’t have to leave his gambling table to eat."

    "The Four Corners is the only spot in the US where you can stand in four states at once: Utah, Colorado, Arizona and New Mexico."

    "The original name for the search engine Google was Backrub. It was renamed Google after the googol, which is the number one followed by 100 zeros."

    "The heart of the blue whale, the largest animal on earth, is five feet long and weighs 400 pounds. The whale in total weighs 40,000 pounds."

    "For comparison, an elephant’s heart weighs around 30 pounds. And a human heart? A mere 10 ounces."

    "The platypus doesn’t have a stomach at all: Their esophagus goes straight to their intestines."

    "Polar bears have black skin. And actually, their fur isn’t white—it’s see-through, so it appears white as it reflects light."

    "Mosquitoes are the deadliest animal in the world: They kill more people than any other creature, due to the diseases they carry."

    "The green code in The Matrix was actually created from symbols in the code designer’s wife’s sushi cookbook."

    "The wedding of Princess Diana and Prince Charles was watched by 750 million people worldwide in 1981; sadly, 2.5 billion watched her funeral in 1997"

    "There are no muscles in your fingers: Their function is controlled by muscles in your palms and arms."

    "The origin of the word “sinister” reflects a historical bias against left-handed people. It comes from the Latin word for “left,” which was also seen to be unlucky or evil."

    "German chocolate cake doesn’t come from Germany. It was named for a person, Sam German, who created a type of baking chocolate for Baker’s in 1852"

    "Hawaiian pizza was created in Ontario, Canada, by Greek immigrant Sam Panopoulos in 1962"

    "Almost all commercially grown artichokes, 99.9 percent, come from California. One town in particular, Castroville, is nicknamed “the Artichoke Capital of the World."

    "The difference between jam and jelly is that jam is made with mashed up fruit while jelly is made with fruit juice"
]


def write(text):
    sys.stdout.write(text)


def clear():
    sys.stdout.write("\033[2J\033[H")


def countdown(num, text):
    for i in range(num, 0, -1):
        clear()
        print(boot + "Your sentence is: " + red + underline + text + boot)
        print(str(i))
        time.sleep(1)


create_table()

ready = input(
    underline + green + "Fast & Furious Typing by group 6\n\n" + boot + "Complete the sentence then you will be able to see your results.\nIt will all become clear.\n\nGet set go!! (Click return)")

attempt = 0
TotalWPM = 0
BestWPM = 0

totalAccuracy = 0

start = "y"

while start == "y":
    # chooses the random passage
    passage = random.choice(passages)

    countdown(3, passage)

    complete = False
    PresentChar = 0
    wrong = 0
    time1 = time.time()
    while not complete:
        if PresentChar > 0:
            # if the letter isn't the first one in the string, then dim all the letters before the current one
            ErrorDetect = boot + shade + passage[PresentChar]
        # underline the current letter
        current = underline + blue + passage[PresentChar]
        # reset the colour for all the ones after the current letter
        afterCurrent = boot + passage[PresentChar + 1:]

        clear()
        if PresentChar == 0:
            print(current + afterCurrent)
        else:
            print(ErrorDetect + current + afterCurrent)

        # detects what key is pressed
        inputChar = getkey()
        while inputChar != passage[PresentChar]:
            # if you put the wrong letter in
            wrong += 1
            # underlines the current letter, showing that you have got it wrong
            current = underline + red + passage[PresentChar]
            clear()
            if PresentChar == 0:
                print(current + afterCurrent)
            else:
                print(ErrorDetect + current + afterCurrent)

            # input the letter again
            inputChar = getkey()

        # have they gone through the whole passage
        if PresentChar >= len(passage) - 1:
            complete = True

        # increments the current letter variable
        PresentChar += 1

    # all the calculations
    attempt += 1
    time2 = time.time()
    clear()
    timeTaken = (time2 - time1) / 60

    wpm = round((len(passage) / 5) / timeTaken)
    TotalWPM += wpm
    if wpm > BestWPM:
        BestWPM = wpm
    average = round(TotalWPM / attempt)
    accuracy = round(100 - ((wrong / (len(passage) + wrong)) * 100))
    totalAccuracy += accuracy
    avrgAcc = round(totalAccuracy / attempt)

    inpu = input('Enter Your name')

    insert_table(inpu, accuracy)

    text = boot + "CONGRATS,You have completed!\n\nWPM: " + green + str(wpm) + boot + "\nAverage WPM: " + green + str(
        average) + boot + "\nYour Highest: " + green + str(BestWPM) + boot + "\n\nAccuracy: " + green + str(
        accuracy) + "%" + boot + "\nAverage Accuracy: " + green + str(avrgAcc) + "%\n"

    print(text)

    play = input("Play again or see Creators? (y/l/n)").lower()
    while play not in ["y", "l", "n"]:
        clear()
        print(text)
        play = input("Play again or see Creators? (y/l/n)").lower()
    if play == "l":
        Creators = underline + red + "Creator (Group 6)\n" + boot + "1. " + blue + "Aneed \n" + boot + "2. " + blue + "Jordan \n" + boot + "3. " + blue + "Alen \n" + boot + "4. " + blue + "Alen\n" + boot
        clear()
        print(Creators)
        play = input("Play again? (y/n)").lower()
        while play not in ["y", "n"]:
            clear()
            print(Creators)
            play = input("Play again? (y/n)").lower()

clear()
print(green + "BYE!!!!" + boot + "\n\n\nComment your highscores!\n\nUpvote if you had fun\n\n:)")
