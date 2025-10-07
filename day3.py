# ============================================================
# TEMAT 2
# ============================================================
# Zadanie 1
# Liczba poziomów powinna być pobierana z klawiatury.
# Choinka o parzystej liczbie poziomów powinna zostać "wyrysowana" gwiazdkami,
# a o nieparzystej - hashami (#).
# Rysowanie choinek ma być powtarzane (w pętli while) aż do wyrysowania choinki o wysokości 7.
# Rysowanie pojedynczej choinki powinno być zawarte w jednej pętli for
# (z użyciem range oraz 'mnożenia liczby przez napis').

while True:
    wysokosc = int(input("Podaj wysokość choinki (7 = koniec): "))
    
    if wysokosc % 2 == 0:
        znak = '*'
    else:
        znak = '#'
    
    for i in range(wysokosc):
        print(' ' * (wysokosc - i - 1), end='')
        print(znak * (2 * i + 1))
    
    if wysokosc == 7:
        print("Koniec działania pętli.")
        break

# ============================================================
# Zadanie 2
# Program wylosuje liczbę całkowitą z zakresu 1–10 i pozwoli na zgadnięcie w 3 próbach.
# Po każdej próbie informuje, czy liczba jest większa czy mniejsza.
# Po 3 nieudanych próbach wyświetla komunikat o porażce (while-else).
# ============================================================

import random

x = random.randint(1, 10)
tries = 3

while tries > 0:
    num = int(input("Podaj liczbę od 1 do 10: "))

    if num == x:
        print("Zgadłeś!")
        break
    elif num < x:
        print("Podana liczba jest za mała.")
    else:
        print("Podana liczba jest za duża.")

    tries -= 1
else:
    print("Nie zgadłeś. Wylosowana liczba to:", x)

# ============================================================
# Zadanie 3
# Program zlicza, ile liter 'A' i 'a' znajduje się w napisie wprowadzonym z klawiatury.
# Wykorzystuje pętlę for i jedno if, bez range, lower, count.
# ============================================================

znaki = input("Podaj ciąg znaków: ")
l = 0

for znak in znaki:
    if znak == 'A' or znak == 'a':
        l += 1

print("Liczba wystąpień liter 'A' i 'a':", l)

# ============================================================
# Zadanie 4
# Program wypisuje pozycje (indeksy) liter 'A' i 'a' w podanym napisie.
# Nie używa range ani działań arytmetycznych (zamiast tego enumerate).
# ============================================================

znaki = input("Podaj ciąg znaków (do sprawdzenia indeksów liter A/a): ")

for index, znak in enumerate(znaki, start=1):
    if znak in ('A', 'a'):
        print("Litera 'A' lub 'a' na pozycji:", index)
