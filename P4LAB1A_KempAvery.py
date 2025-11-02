import turtle as t

t.speed(5)

for i in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(150, 0)
t.pendown()

i = 0
while i < 3:
    t.forward(100)
    t.right(120)
    i += 1

t.hideturtle()
t.done()
