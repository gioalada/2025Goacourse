import turtle

# ეკრანის ინიციალიზაცია
screen = turtle.Screen()
screen.bgcolor("sky blue")

# კალამი შექმნა
pen = turtle.Turtle()
pen.speed(10)

# სასახლის საფუძველი
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# სასახლის გალერეა
def draw_tower():
    # კოშკის თავი
    pen.penup()
    pen.goto(-20, 100)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("gray")
    for _ in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()

    # კოშკის კედლები
    pen.penup()
    pen.goto(-30, 100)
    pen.pendown()
    pen.setheading(90)
    pen.begin_fill(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(60)
    pen.end_fill()

# GOA-ს დროშა
def draw_goa_flag():
    pen.penup()
    pen.goto(-10, 180)
    pen.pendown()
    pen.setheading(0)
    pen.begin_fill()
    pen.fillcolor("orange")
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.end_fill()

    # ქვედა ნაწილი
    pen.penup()
    pen.goto(-10, 170)
    pen.pendown()
    pen.setheading(0)
    pen.begin_fill()
    pen.fillcolor("green")
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.end_fill()

# სასახლის კედლები
draw_rectangle("light gray", -100, -100, 200, 100)

# კოშკი და დროშა
draw_tower()
draw_goa_flag()

# დაბლა მწვანე ბალახი
pen.penup()
pen.goto(-150, -100)
pen.pendown()
pen.begin_fill()
pen.fillcolor("green")
pen.forward(300)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(50)
pen.end_fill()

# პროგრამის დასრულება
pen.hideturtle()
turtle.done()
