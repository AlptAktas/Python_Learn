import pandas as pd
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.DataFrame(pd.read_csv("Day_25/day-25-us-states-game-start/50_states.csv"))
all_states = data.state.to_list()
guessed_states = []




while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        if answer_state in guessed_states:
            continue
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())





#turtle.mainloop()
