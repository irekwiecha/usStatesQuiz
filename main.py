import turtle
import pandas as pd

DATA = "50_states.csv"
IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(width=760, height=493)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states = pd.read_csv(DATA)
all_states = states.state.to_list()

guessed = []
while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed]
        to_learn = pd.Series(missing_states, name="state_to_learn")
        to_learn.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.iloc[0, 1]), int(state_data.iloc[0, 2]))
        t.write(answer_state)
        guessed.append(answer_state)
