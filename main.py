# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import turtle
import pandas as pd

# Setting up the Screen and Turtle object
s = turtle.Screen()
s.title("US' States Name Quiz")
writer = turtle.Turtle()
writer.color("black")
writer.hideturtle()
writer.penup()

# Display the background Image
image = "states.gif"
s.addshape(image)
turtle.shape(image)

# Game Data
data = pd.read_csv("states.csv")
states_list = data["State"].to_list()
guessed_states = []

while len(guessed_states) > 50:
    query = turtle.textinput(f"{len(guessed_states)}/50 States Correct", "Guess The Name Of A State: ").title()
    
    if query == 'Exit':
        missed_states = [state for state in states_list if state not in guessed_states]
        missed_states_list = pd.DataFrame(missed_states, columns=["State"])
        missed_states_list.to_csv("missed_states.csv")
        break

    # Checking the answer
    if query in states_list:
        guessed_states.append(query)
        state_data = data[data.State == query]
        writer.goto(int(state_data.X), int(state_data.Y))
        writer.write(query, font=("Verdana", 10, "normal"))



s.mainloop()