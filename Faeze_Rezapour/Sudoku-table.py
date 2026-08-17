import turtle

CELL = 40
N = 9
SIZE = CELL * N

t = turtle.Turtle()
t.hideturtle()
t.shape("blank")
t.speed(0)
turtle.tracer(0, 0)

start_x, start_y = -SIZE / 2, SIZE / 2

# حلقهٔ دوبخشی: در هر تکرار، هم خطوط عمودی هم افقی رسم می‌شوند
for direction in range(2):  # 0=عمودی ، 1=افقی
    for i in range(N + 1):
        t.penup()
        # تعیین موقعیت شروع و زاویه
        if direction == 0:  # عمودی
            t.goto(start_x + i * CELL, start_y)
            t.setheading(270)
        else:                # افقی
            t.goto(start_x, start_y - i * CELL)
            t.setheading(0)

        # تعیین ضخامت بر اساس موقعیت خط
        if i == 0 or i == N:
            t.pensize(5)
        elif i % 3 == 0:
            t.pensize(3)
        else:
            t.pensize(1)

        t.pendown()
        t.forward(SIZE)
        t.penup()

# قاب بیرونی ضخیم برای زیبایی و تأکید
t.pensize(5)
t.penup()
t.goto(start_x, start_y)
t.pendown()
for _ in range(4):
    t.forward(SIZE)
    t.right(90)

turtle.update()
turtle.done()