
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

size = 40

for i in range(10):
    if i == 0 or i == 9:
        t.pensize(5)
    elif i % 3 == 0:
        t.pensize(3)
    else:
        t.pensize(1)

    t.penup()
    t.goto(-180 + i * size, -180)
    t.pendown()
    t.goto(-180 + i * size, 180)


for i in range(10):

    if i == 0 or i == 9:
        t.pensize(5)
    elif i % 3 == 0:
        t.pensize(3)
    else:
        t.pensize(1)

    t.penup()
    t.goto(-180, -180 + i * size)
    t.pendown()
    t.goto(180, -180 + i * size)

for row in range(9):
    for col in range(9):

        number = random.randint(1, 9)

        x = -160 + col * size
        y = 145 - row * size

        t.penup()
        t.goto(x, y)
        t.write(number, align="center", font=("Arial", 15, "normal"))

turtle.done()