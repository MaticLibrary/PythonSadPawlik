PRAKTYCZNY PORADNIK
Haskell w Pythonie – od zera do bohatera
CZĘŚĆ 1: ABSOLUTNE PODSTAWY
Co to za moduł?
# To NIE jest prawdziwy Haskell, tylko emulacja w Pythonie!
# Pozwala pisać kod w stylu funkcyjnym
from haskell import *

Podstawowe importy do 95% zadań
from haskell import add, mul, pow, truediv, eq, gt, lt, map, filter, sum, flip

CZĘŚĆ 2: 4 ŻELAZNE ZASADY
Zasada 1: Funkcje są CURRIED
# Normalna funkcja: add(2, 3) → 5
# W tym module: add(2)(3) → 5

add_5 = add(5)
print(add_5(10))  # 15

Zasada 2: FLIP odwraca argumenty
# truediv(8, 2) = 4
# flip(truediv)(8, 2) = truediv(2, 8) = 0.25

divide_by_2 = flip(truediv)(2)   # x → x / 2
greater_than_3 = flip(gt)(3)     # x → x > 3

Zasada 3: ** to złożenie (od tyłu)
f = lambda x: x * 2
g = lambda x: x + 3

h = f ** g
print(h(5))  # 16

Zasada 4: map / filter zwracają iteratory
add_1 = map(add(1))
result = add_1([1, 2, 3])
print(list(result))  # [2, 3, 4]

CZĘŚĆ 3: ROZWIĄZANIA ZADAŃ
Zadanie 1: Kwadraty liczb ujemnych
from haskell import sum, map, filter, gt, flip, pow

filtruj_ujemne = filter(gt(0))
kwadrat = map(flip(pow)(2))
suma = sum

suma_kwadratow = suma ** kwadrat ** filtruj_ujemne
print(suma_kwadratow([1, -2, 3, -4]))  # 20

Zadanie 2: (x + 3) / 2
from haskell import map, add, truediv, flip
dodaj_3 = add(3)
podziel_2 = flip(truediv)(2)
wynik_A = map(podziel_2 ** dodaj_3)
map_dodaj = map(add(3))
map_podziel = map(flip(truediv)(2))
wynik_B = map_podziel ** map_dodaj

lista = [1, 2, 3]
print(list(wynik_A(lista)))
print(list(wynik_B(lista)))

Zadanie 3: Indeksy wystąpień elementu
from haskell import map, filter, eq, Haskell

def pierwszy(p):
    return p[0]

@Haskell
def drugi(p):
    return p[1]

def znajdz_indeksy(lista, szukany):
    return (map(pierwszy) ** filter(eq(szukany) ** drugi))(list(enumerate(lista)))

print(list(znajdz_indeksy([1, 2, 3, 3, 2, 1], 3)))

CZĘŚĆ 4: GOTOWE WZORY
suma_kwadratow = sum ** map(flip(pow)(2))
wieksze_od = lambda n: filter(flip(gt)(n))
dodaj_do_wszystkich = lambda n: map(add(n))
przetworz = lambda warunek, funkcja: map(funkcja) ** filter(warunek)

CZĘŚĆ 5: NAJCZĘSTSZE BŁĘDY
Dzielenie
zle = truediv(2)
dobrze = flip(truediv)(2)

Porównania
zle = gt(3)
dobrze = flip(gt)(3)

Potęgowanie
zle = pow(2)
dobrze = flip(pow)(2)

Brak list()
wynik = map(add(1))([1, 2, 3])
print(list(wynik))

CZĘŚĆ 6: STRATEGIA ROZWIĄZYWANIA ZADAŃ
Określ wejście i wyjście
Rozbij problem na filter / map / sum
Składaj funkcje od końca
Testuj na małych danych

CZĘŚĆ 7: ZADANIA
Suma pierwiastków liczb parzystych
from haskell import sum, map, filter, pow, flip, Haskell

@Haskell
def parzysta(x):
    return x % 2 == 0
    
rozwiazanie = sum ** map(flip(pow)(0.5)) ** filter(parzysta)
Mapa: x³ + 10
from haskell import map, add, flip, pow
potega_3 = flip(pow)(3)
dodaj_10 = add(10)
rozwiazanie = map(dodaj_10 ** potega_3)

CZĘŚĆ 8: OSTRZEŻENIA
To nie jest prawdziwy Haskell
Brak leniwego obliczania
Brak typów statycznych
Brak monad

CZĘŚĆ 9: CHEAT-SHEET
add(N)
mul(N)
flip(pow)(N)
flip(truediv)(N)
flip(gt)(N)
flip(lt)(N)
eq(N)
f ** g
map(f)

filter(w)

sum
