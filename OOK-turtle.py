import turtle as t

def rectangle(horinzontal, vertical, color):
    t.pendown()
    t.pensize()
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horinzontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('normal')
t.bgcolor('Dodger blue')
t.shape('turtle')



#jalkaterät
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

#jalat
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

#ruumis
t.goto(-90, 100)
rectangle(100, 150, 'red')

#käsivarret
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')

t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')

#kaula
t.goto(-50, 120)
rectangle(15,40, 'red')

#pää
t.goto(-85, 170)
rectangle(80, 50, 'yellow')

#silmät
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')

#suu
t.goto(-65, 135)
rectangle(40, 5, 'black')

t.hideturtle()

while True:
    pass
