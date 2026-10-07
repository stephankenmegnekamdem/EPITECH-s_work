import turtle

def draw_polygon(n):

    cursor = turtle.Turtle()

    for i in range(n):

        cursor.forward(10)
        cursor.right(360/n)

    turtle.done()

sides=int(input("Enter sides of polygon: "))
draw_polygon(sides)