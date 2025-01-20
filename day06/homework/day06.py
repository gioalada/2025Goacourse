x = 10  # პირველი მნიშვნელობა
x += 5  # 1-ლი შეცვლა: x = 10 + 5 = 15
x -= 3  # 2-რი შეცვლა: x = 15 - 3 = 12
x *= 2  # 3-დე შეცვლა: x = 12 * 2 = 24
x /= 4  # 4-წელი შეცვლა: x = 24 / 4 = 6
x += 10  # 5-ლი შეცვლა: x = 6 + 10 = 16

print(x)  # საბოლოოდ დაბეჭდავს 16



import turtle

# ეკრანის კონფიგურაცია
screen = turtle.Screen()
screen.bgcolor("lightblue")

# ქმნით მარშრუტს
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)
pen.color("orange")

# პირველი წრე
pen.penup()
pen.goto(0, -100)  # წრის დაწყების პოზიცია
pen.pendown()
pen.circle(100)

# დარჩენილი 5 წრე
for _ in range(5):
    pen.penup()
    pen.forward(40)  # გადავა წინ 40 პიქსელი
    pen.pendown()
    pen.circle(100)

# დამთავრება
turtle.done()
