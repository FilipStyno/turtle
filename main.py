from turtle import *
import zelva  # Importuje modul 'zelva', kde jsou definované funkce pro kreslení


def menu():
    """
    Zobrazí nabídku s možnostmi pro uživatele a vrátí uživatelem zadané číslo.
    Pokud je číslo mimo rozsah 0-5, upozorní na nesprávný vstup.
    """
    num = int(input("1. Spirala\n"
                    "2. Trojuhelnik\n"
                    "3. Barevny destnik\n"
                    "4. Srdicko\n"
                    "5. Hvezda\n"
                    "Zadej '0' pro ukonceni programu\n"
                    "Vyber jednu z moznosti: "))

    # Zkontroluje, zda je vstupní číslo v povoleném rozsahu
    if num < 0 or num > 5:
        print("Zadej cislo v rozsahu 1-5")
        return None  # Vrátí None, pokud je zadáno číslo mimo rozsah

    return num  # Vrátí číslo vybrané uživatelem


# Zavolá funkci menu a uloží výsledek do proměnné 'x'
x = menu()

# Pokud uživatel zadá 0, program se ukončí
if x == 0:
    exit()

# Podmínky pro různé volby uživatele, zavolají odpovídající funkci z modulu 'zelva'
elif x == 1:
    zelva.spirala()  # Kreslí spirálu

elif x == 2:
    zelva.triangle()  # Kreslí trojúhelník

elif x == 3:
    zelva.umbrella()  # Kreslí barevný deštník

elif x == 4:
    zelva.heart()  # Kreslí srdce

elif x == 5:
    zelva.star()  # Kreslí hvězdu

# Umožňuje, aby okno s kresbou zůstalo otevřené, dokud ho uživatel nezavře
mainloop()
