import turtle

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

turtle.speed(3)
turtle.bgcolor("white")
turtle.pencolor("blue")

draw_star(100)

turtle.done()