import turtle

def draw_spiral_square(turns):
    cursor = turtle.Turtle()

    length = 20

    for i in range(turns * 4):
        cursor.forward(length)
        cursor.right(90)
        length += 10

    turtle.done()

def draw_spiral_circle(turns):
    cursor = turtle.Turtle()
    cursor.color("blue")
    for i in range(turns):
        radius = 5 + i * 5
        cursor.circle(radius, 90)

    turtle.done()

draw_spiral_circle(20)

draw_spiral_square(5)

