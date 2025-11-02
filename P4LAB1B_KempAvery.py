import turtle as t

FIRST = "A"    
LAST  = "K"     

t.speed(6)
t.pensize(5)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_A(size=80):
    t.setheading(75)
    t.forward(size)
    t.setheading(-75)
    t.forward(size)
    t.backward(size / 2)
    t.setheading(180)
    t.forward(size / 3)
    t.setheading(0)
    
def draw_K(size=80):
    t.setheading(90)
    t.forward(size)
    t.backward(size / 2)
    t.setheading(45)
    t.forward(size / 1.5)
    t.backward(size / 1.5)
    t.setheading(-45)
    t.forward(size / 1.5)

def draw_letter(letter):
    if letter == "A":
        draw_A()
    elif letter == "K":
        draw_K()
    else:
        for _ in range(2):
            t.forward(60)
            t.left(90)
            t.forward(100)
            t.left(90)

move(-120, -40)
draw_letter(FIRST)

t.penup()
t.forward(120)
t.pendown()

draw_letter(LAST)

t.hideturtle()
t.done()
