import turtle

def draw_batman_sign():

    window=turtle.Screen()
    window.bgcolor("black")
    cursor=turtle.Turtle()
    cursor.color("yellow")

    cursor.begin_fill()
    cursor.left(90)
    cursor.circle(-30, 180)

    cursor.right(90)
    cursor.circle(35, 90)
    cursor.circle(100, 90)
    cursor.circle(170, 98)
    cursor.right(282)
    cursor.circle(-80, 75)
    cursor.right(100)
    cursor.forward(100)
    cursor.left(135)
    cursor.forward(50)
    cursor.right(45)
    cursor.forward(25)
    cursor.penup()
    cursor.goto(0, 0)
    cursor.pendown()
    cursor.end_fill()
    turtle.done()



import turtle

import turtle

def draw_oval_circle():
    window = turtle.Screen()
    cursor = turtle.Turtle()
    cursor.color("purple")
    cursor.speed(0)

    for i in range(180):
        cursor.penup()
        cursor.goto(0, 0)          # go back to the center
        cursor.setheading(i * 10+i)  # point in this oval's direction
        cursor.forward(150)        # move out, leaving the middle empty
        cursor.pendown()

        cursor.circle(120, 45)
        cursor.circle(10, 45)
        cursor.circle(10, 45)
        cursor.circle(120, 45)
        cursor.circle(120, 45)
        cursor.circle(10, 45)
        cursor.circle(10, 45)
        cursor.circle(120, 45)     # stops early: the oval is not closed

    turtle.done()


#draw batman_sign
for _ in range(36):
    turtle.circle(80)
    turtle.left(10)
turtle.done()