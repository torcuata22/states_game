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

# turtle.onscreenclick(get_mouse_click_coor) #onscreenclick is an event listener, waits for click to pass function that print coordinates to console
# turtle.mainloop() #alternative way of keeping screen open


data = pd.read_csv("50_states.csv")
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

#To do:
# Guess to title case (use .title()?)

#Check if answer_state is among the 50 states: pandas isin() function?

#get ahold of all states as a list:
all_states = data.state.to_list #transforms the data series into a list



#If guess is correct, write it on the map: update screen to add text using coordinates from dataset?

#Loop (keep guessing until thye get all 50 states): use while loop (until len(right_answers)=50?)

#Add correct guesses to list (can't guess same state twice): append()

#Keep score create scoreboard, score variable, display it and update it




screen.exitonclick()
