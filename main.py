import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_states_list = []

mac = turtle.Turtle()
mac.penup()
mac.hideturtle()

count = 0

while count < 50:
    answer = screen.textinput(title=f"{count}/50 States Correct", prompt="What is the state name").title()
    if answer == "Exit":
        break
    if answer in states_list:
        correct_states_list.append(answer)
        count += 1
        data_row = data[data.state == answer]
        mac.setpos(int(data_row.x), int(data_row.y))
        mac.write(answer, align="center", font=('Arial', 15, 'normal'))

for state in correct_states_list:
    states_list.remove(state)

new_data = pandas.DataFrame(states_list)
new_data.to_csv("states_to_learn")


print(states_list)
