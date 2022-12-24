import turtle
import pandas as pd



image = "blank_states_img.gif"
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("U.S States Game")
#To add image in Turtle: load image as shape (makes it avainlable as a shape for the turtle)
screen.addshape(image)
turtle.shape(image)

#This is how you can figure out coordinates of each state:
# def get_mouse_click_coor(x,y):
#     print(x,y)

#turtle.onscreenclick(get_mouse_click_coor) #onscreenclick is an event listener, waits for click to pass function that print coordinates to console
#turtle.mainloop() #alternative way of keeping screen open


data = pd.read_csv("50_states.csv")

all_states = data["state"].to_list() 
guessed_states=[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    guessed_states.append(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            df = pd.DataFrame(missing_states)
            file = df.to_csv("States_to_learn.csv")
            
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) #can also use state_data.state.item()









screen.exitonclick()
