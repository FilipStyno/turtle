import turtle
from turtle import *
import zelva
def menu():
    num = int(input("1. Spirala\n"
                    "2. Trojuhelnik\n"
                    "3. Barevny destnik\n"
                    "4. Srdicko\n"
                    "5. Hvezda\n"
                    "Zadej '0' pro ukonceni programu\n"
                    "Vyber jednu z moznosti: "))

    if num < 0 or num > 5:
        print("Zadej cislo v rozsahu 1-5")
        return None

    return num

x = menu()
if x == 0:
    exit()

elif x == 1:
    zelva.spirala()

elif x == 2:
    zelva.triangle()

elif x == 3:
    zelva.umbrella()

elif x == 4:
    zelva.heart()

elif x == 5:
    zelva.star()
mainloop()