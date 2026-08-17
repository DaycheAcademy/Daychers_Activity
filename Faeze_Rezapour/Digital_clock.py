import time
import turtle

def draw_box(turtle_obj, x=-220, y=-60, w=440, h=120, pensize=3):
    turtle_obj.hideturtle()
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.pensize(pensize)
    for _ in range(2):
        turtle_obj.forward(w)
        turtle_obj.left(90)
        turtle_obj.forward(h)
        turtle_obj.left(90)
    turtle_obj.penup()

def show_clock(screen, writer):
    now = time.strftime("%H:%M:%S")   # زمان سیستم
    writer.clear()
    writer.goto(0, -30)
    writer.write(now, align="center", font=("Arial", 40, "normal"))
    screen.ontimer(lambda: show_clock(screen, writer), 1000)

if __name__== "__main__":
    screen = turtle.Screen()
    screen.title("ساعت دیجیتال")
    screen.setup(600, 250)
    screen.bgcolor("white")

    box_t = turtle.Turtle()
    draw_box(box_t)

    t = turtle.Turtle()
    t.hideturtle()
    t.color("black")
    t.penup()

    show_clock(screen, t)
    screen.mainloop()