import turtle
import time

t = turtle.Turtle()
t.hideturtle()

while True:
    t.clear()
    t.write(time.strftime("%H:%M:%S"), align="center", font=("Arial", 100, "normal"))
    time.sleep(1)