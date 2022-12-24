import turtle 



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

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
screen.exitonclick()
