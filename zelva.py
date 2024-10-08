from turtle import *

def curve():
    for i in range(200):
        # Defining step by step curve motion
        right(1)
        forward(1)
def spirala():
    for i in range(100):
        forward(i)
        left(50)
def triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(110)

def umbrella():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            speed(0)
            color(c)
            forward(steps)
            right(30)
            color('red')

def heart():
    speed(0)
    fillcolor('red')
    begin_fill()
    left(140)
    forward(113)
    curve()
    left(120)
    curve()
    forward(112)
    end_fill()

def star():
    penup()
    goto(145, -130)

    fillcolor("yellow")
    begin_fill()

    for i in range(5):
        fd(100)
        rt(144)

    end_fill()
    pendown()