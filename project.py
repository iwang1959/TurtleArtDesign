import turtle
bob=turtle.Turtle()
from myShape import*
from random import randint
bob.speed(0)
turtle.tracer(0)
turtle.colormode(255)
turtle.bgcolor("green")
bob.shape("turtle")

for times in range(50):
    bob.color(255,69,0)
    bob.circle(900)
    bob.left(125)
    bob.width(10)

for times in range(50):
    bob.color("black")
    bob.circle(500)
    bob.left(50)

for times in range(100):
    bob.circle(100)
    bob.left(5)
    bob.color("black")

for times in range(200):
    bob.width(10)
    bob.circle(100000)
    bob.left(10)
    bob.color(255-times,0,55+times)

for times in range(300):
    x =randint(-1000, 1200)
    y =randint(-1000, 1200)
    star(bob,5)
    move(bob,x,y)
    bob.color("yellow")

for times in range(500):
    x =randint(-1000, 1200)
    y =randint(-1000, 1200)
    bob.color("white")
    move(bob,x,y)
    bob.circle(1)

