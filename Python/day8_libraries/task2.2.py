#makes 3 circles each time turning at 90 degrees right from where it ended the last circle


import turtle # this is our library

toto = turtle.Screen()    # this will control the screen
toto.bgcolor("black")     #we want a black screen


titi = turtle.Turtle()    # this controls the turtle object
titi.color("red")         # turtle should be red(leave behind red

for i in range(3):       #for 3 turns,

    titi.right(90)  #it turns right at an angle of 90 degrees
    titi.circle(42)      #then makes a cirle of 42 diameter


toto.exitonclick() #then we can exit the screen on a  click