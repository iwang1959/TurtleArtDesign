def square( t, distance ):
    for times in range(4):
        t.forward(distance)
        t.left(90)
def triange(t):
    for times in range(3):
        t.forward(120)
        t.left(120)
def pentagon (t, distance):
    angle=360/5
    for times in range (5):
        t.forward(distance)
        t.left(angle)

def polygon (t, distance , side):
    angle=360/side
    t.begin_fill()
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def move ( t , x , y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def star(t,distance):
    for times in range (6):
        t.forward(distance)
        t.left(135)
