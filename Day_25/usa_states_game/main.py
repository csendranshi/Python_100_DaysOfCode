import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
correct_answers = []
score =0

turtle.shape(image)
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 states guessed", prompt="What's another state's name?").title()
    print(correct_answers)

    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x),float(state_data.y))
        t.write(answer_state)
        score += 1
        correct_answers.append(answer_state)

    if answer_state == "Exit":
        remaining_states = []
        for state in states:
            if state not in correct_answers:
                remaining_states.append(state)
        print(remaining_states)
        new_data = pd.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break
