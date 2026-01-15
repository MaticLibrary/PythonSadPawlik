from haskell import *
from functools import reduce
import math

# ====================================================================
# 2. CEZAR i inne
# ====================================================================

# CEZAR (wersja z kompozycją funkcji)
@Haskell
def nakod(c):
    return ord(c)

@Haskell
def naznaki(k):
    return chr(k)

def Cezar(napis, klucz):
    return map(naznaki ** (flip(mod)(127)) ** add(klucz) ** nakod)(napis)

# DODAJ: funkcja dodająca 7 do każdego elementu listy
dodaj_7 = map(add(7))

# SUMA PARZYSTYCH (rekurencja)
def suma_parzystych(lst, suma=0):
    match lst:
        case []:
            return suma
        case [glowa, *ogon]:
            if glowa % 2 == 0:
                suma += glowa
            return suma_parzystych(ogon, suma)

# EUKLIDES (odległość euklidesowa między dwiema listami)
def Euklides(lst1, lst2):
    return math.sqrt(reduce(lambda acc, x: acc + ((x[0] - x[1]) ** 2), zip(lst1, lst2), 0))

# ====================================================================
# 3. MNOŻENIE i inne
# ====================================================================

# MNOŻENIE każdego elementu przez 3
x = map(mul(3))

# FILTROWANIE WARTOŚCI W ZAKRESIE
def filtruj_wartosci(min_val, max_val, lista):
    def filtruj(nowa_lista, ele):
        if min_val <= ele <= max_val:
            nowa_lista.append(ele)
        return nowa_lista
    return reduce(filtruj, lista, [])

# REKURENCYJNA SUMA KROTEK
def suma_krotek(lista):
    if not lista:
        return []
    suma_biezaca = sum(lista[0])
    return [suma_biezaca] + suma_krotek(lista[1:])

# ====================================================================
# 4. DZIELENIE i inne
# ====================================================================

# DZIELENIE każdego elementu przez 3
x = map(truediv(3))

# MAKSIMUM z użyciem reduce
def maksimum(lista):
    return reduce(lambda max_wartosc, ele: max_wartosc if max_wartosc > ele else ele, lista)

# REKURENCYJNY ILOCZYN
def iloczyn_rekurencyjny(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista[0] * iloczyn_rekurencyjny(lista[1:])

# USUWANIE SAMOGŁOSEK
def del_samogloski(napisy):
    return list(map(lambda napis: ''.join(filter(lambda litera: litera not in "aeouiy", napis)), napisy))

# ====================================================================
# 5. POTĘGA i inne
# ====================================================================

# POTĘGA: podniesienie każdego elementu do kwadratu
x = map(flip(pow)(2))

# REKURENCYJNA ŚREDNIA I WARIANCJA
def rekurencyjna_srednia_wariancja(lista, dlugosc, suma=0):
    if not lista:
        if dlugosc > 0:
            srednia = suma / dlugosc
        else:
            srednia = 0
        return srednia, 0
    srednia, wariancja = rekurencyjna_srednia_wariancja(lista[1:], dlugosc, suma + lista[0])
    if dlugosc > 0:
        wariancja += ((lista[0] - srednia) ** 2) / dlugosc
    return srednia, wariancja

# FILTROWANIE WEKTORÓW (list) o długości >= podanej
def filter_vectors(vectors, length):
    return list(filter(lambda vector: len(vector) >= length, vectors))

# SUMOWANIE PAR (listy krotek)
def Sumuj_pary(lista):
    return reduce(lambda nowa_lista, para: nowa_lista + [(para[0] + para[1])], lista, [])

# ====================================================================
# 1. ODEJMOWANIE i inne
# ====================================================================

# ODEJMOWANIE: odjęcie 7 od każdego elementu (używając add z liczbą ujemną)
x = map(add(-7))

# NORMALIZACJA WEKTORA (przy założeniu, że mamy funkcję dlugosc_wektora)
def dlugosc_wektora(wektor):
    return math.sqrt(sum(map(lambda x: x**2, wektor)))

def normalizuj(wektor):
    dlugosc = dlugosc_wektora(wektor)
    return list(map(mul(1 / dlugosc), wektor))

# REKURENCJA OGONOWA: łączenie krotek w jedną listę
def polacz_krotki(krotki, wynik=None):
    if wynik is None:
        wynik = []
    if not krotki:
        return wynik
    return polacz_krotki(krotki[1:], wynik + list(krotki[0]))

# LISTA STRINGÓW BEZ SŁÓW ZACZYNAJĄCYCH SIĘ NA DANĄ LITERĘ
# (wersja z reduce)
def lista_stringow_bez_slow_z_litera(lista_stringow, litera):
    return reduce(
        lambda acc, slowo: acc + [slowo] if (not acc or acc[-1] != slowo) and not slowo.startswith(litera) else acc,
        [slowo for string in lista_stringow for slowo in string.split()],
        []
    )

# ====================================================================
# PRZYKŁADOWE UŻYCIE
# ====================================================================

def main():
    print("=== Testy ===")
    
    # Cezar
    print("Cezar('ABC', 3):", list(Cezar("ABC", 3)))
    
    # Suma parzystych
    print("suma_parzystych([1,2,3,4,5,6]):", suma_parzystych([1,2,3,4,5,6]))
    
    # Euklides
    print("Euklides([1,2,3], [4,5,6]):", Euklides([1,2,3], [4,5,6]))
    
    # Maksimum
    print("maksimum([1,5,3,9,2]):", maksimum([1,5,3,9,2]))
    
    # Iloczyn rekurencyjny
    print("iloczyn_rekurencyjny([1,2,3,4]):", iloczyn_rekurencyjny([1,2,3,4]))
    
    # Sumowanie par
    print("Sumuj_pary([(1,2), (3,4), (5,6)]):", Sumuj_pary([(1,2), (3,4), (5,6)]))
    
    # Normalizacja
    print("normalizuj([3,4]):", normalizuj([3,4]))
    
    # Łączenie krotek
    print("polacz_krotki([(1,2), (3,4), (5,6)]):", polacz_krotki([(1,2), (3,4), (5,6)]))

if __name__ == "__main__":
    main()
