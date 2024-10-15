from turtle import *


def curve():
    """Nakreslí zakřivení."""
    for i in range(200):
        # Posun o 1 stupeň doprava a 1 krok dopředu pro vytvoření křivky
        right(1)
        forward(1)


def spirala():
    """Nakreslí spirálu."""
    for i in range(100):
        forward(i)
        left(50)


def triangle(side_length=100):
    """Nakreslí trojúhelník se specifikovanou délkou stran."""
    for _ in range(3):
        forward(side_length)
        left(120)


def umbrella():
    """Nakreslí deštník."""
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            speed(0)
            color(c)  # Změna barvy pro každý krok
            forward(steps)
            right(30)
            color('red')  # Vždy po kroku se vrátí zpět k červené


def heart():
    """Nakreslí srdce."""
    speed(0)
    fillcolor('red')
    begin_fill()
    left(140)
    forward(113)
    curve()
    left(120)
    curve()       # Zrcadlový tvar pro pravou stranu
    forward(112)
    end_fill()


def star(size=100):
    """Nakreslí hvězdu s možností nastavit velikost."""
    penup()
    goto(145, -130)
    fillcolor("yellow")
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)  # Otočení o 144 stupňů pro pěticípou hvězdu
    end_fill()
    pendown()
