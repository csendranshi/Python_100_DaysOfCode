name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()

digits = [['t','r' ,'u','e'],['l','o','v','e']]
value = [0,0]
for i in range(len(digits)):
    for j in range(len(digits[i])):
        value[i]+=name1.count(digits[i][j])
        value[i]+=name2.count(digits[i][j])
score = int(str(value[0])+str(value[1]))

if (score<10 or score>90):
    print(f"Your score is {score}, you go together like coke and mentos!")
elif (score>=40 and score<=50):
    print(f"Your score is {y}, you are alright together.")
else:
    print(f"Your score is {score}")