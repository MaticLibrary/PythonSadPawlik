from haskell import *
from functools import reduce
import math

# ====================================================================
# 1. SZYFR CEZARA (z kompozycją funkcji)
# ====================================================================

@Haskell
def na_kod(znak):
    return ord(znak)

@Haskell
def na_znak(kod):
    return chr(kod)

def cezar(napis, klucz):
    return map(na_znak ** (flip(mod)(127)) ** add(klucz) ** na_kod)(napis)

# ====================================================================
# 2. DODAJ_7 - funkcja dodająca 7 do każdego elementu listy
# ====================================================================

dodaj_7 = map(add(7))

# ====================================================================
# 3. SUMA PARZYSTYCH (rekurencja ogonowa)
# ====================================================================

def suma_parzystych(lista, suma=0):
    match lista:
        case []:
            return suma
        case [pierwszy_element, *reszta_listy]:
            if pierwszy_element % 2 == 0:
                suma += pierwszy_element
            return suma_parzystych(reszta_listy, suma)

# ====================================================================
# 4. EUKLIDES - odległość euklidesowa między dwiema listami
# ====================================================================

def euklides(lista1, lista2):
    return math.sqrt(reduce(lambda akumulator, para: akumulator + ((para[0] - para[1]) ** 2), zip(lista1, lista2), 0))

# ====================================================================
# 5. POMNOŻ_PRZEZ_3 - każdy element listy pomnożyć przez 3
# ====================================================================

pomnóż_przez_3 = map(mul(3))

# ====================================================================
# 6. FILTRUJ_WARTOŚCI_W_ZAKRESIE (z użyciem reduce)
# ====================================================================

def filtruj_wartości(minimalna_wartość, maksymalna_wartość, lista):
    def filtruj(nowa_lista, element):
        if minimalna_wartość <= element <= maksymalna_wartość:
            nowa_lista.append(element)
        return nowa_lista
    return reduce(filtruj, lista, [])

# ====================================================================
# 7. REKURENCYJNA_SUMA_KROTEK
# ====================================================================

def rekurencyjna_suma_krotek(lista):
    if not lista:
        return []
    suma_bieżąca = sum(lista[0])
    return [suma_bieżąca] + rekurencyjna_suma_krotek(lista[1:])

# ====================================================================
# 8. PODZIEL_PRZEZ_3 - każdy element listy podzielić przez 3
# ====================================================================

podziel_przez_3 = map(truediv(3))

# ====================================================================
# 9. MAKSIMUM z użyciem reduce
# ====================================================================

def maksimum(lista):
    return reduce(lambda maksymalna_wartość, element: maksymalna_wartość if maksymalna_wartość > element else element, lista)

# ====================================================================
# 10. REKURENCYJNY_ILOCZYN
# ====================================================================

def rekurencyjny_iloczyn(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista[0] * rekurencyjny_iloczyn(lista[1:])

# ====================================================================
# 11. USUŃ_SAMOGŁOSKI z napisów
# ====================================================================

def usuń_samogłoski(lista_napisów):
    return list(map(lambda napis: ''.join(filter(lambda litera: litera not in "aeouiy", napis)), lista_napisów))

# ====================================================================
# 12. PODNIEŚ_DO_KWADRATU - podniesienie każdego elementu do kwadratu
# ====================================================================

podnieś_do_kwadratu = map(flip(pow)(2))

# ====================================================================
# 13. REKURENCYJNA_ŚREDNIA_I_WARIANCJA
# ====================================================================

def rekurencyjna_średnia_i_wariancja(lista, długość, suma=0):
    if not lista:
        if długość > 0:
            średnia = suma / długość
        else:
            średnia = 0
        return średnia, 0
    średnia, wariancja = rekurencyjna_średnia_i_wariancja(lista[1:], długość, suma + lista[0])
    if długość > 0:
        wariancja += ((lista[0] - średnia) ** 2) / długość
    return średnia, wariancja

# ====================================================================
# 14. FILTRUJ_WEKTORY o długości >= podanej
# ====================================================================

def filtruj_wektory(lista_wektorów, minimalna_długość):
    return list(filter(lambda wektor: len(wektor) >= minimalna_długość, lista_wektorów))

# ====================================================================
# 15. SUMUJ_PARY (listy krotek) z użyciem reduce
# ====================================================================

def sumuj_pary(lista):
    return reduce(lambda nowa_lista, para: nowa_lista + [(para[0] + para[1])], lista, [])

# ====================================================================
# 16. ODEJMIJ_7 - odjęcie 7 od każdego elementu
# ====================================================================

odejmij_7 = map(add(-7))

# ====================================================================
# 17. DŁUGOŚĆ_WEKTORA
# ====================================================================

def długość_wektora(wektor):
    return math.sqrt(sum(map(lambda x: x**2, wektor)))

# ====================================================================
# 18. NORMALIZUJ_WEKTOR
# ====================================================================

def normalizuj_wektor(wektor):
    długość = długość_wektora(wektor)
    return list(map(mul(1 / długość), wektor))

# ====================================================================
# 19. REKURENCYJNE_ŁĄCZENIE_KROTEK w jedną listę
# ====================================================================

def rekurencyjne_łączenie_krotek(lista_krotek, wynik=None):
    if wynik is None:
        wynik = []
    if not lista_krotek:
        return wynik
    return rekurencyjne_łączenie_krotek(lista_krotek[1:], wynik + list(lista_krotek[0]))

# ====================================================================
# 20. LISTA_NAPISÓW_BEZ_SŁÓW_Z_POCZĄTKOWĄ_LITERĄ
# ====================================================================

def lista_napisów_bez_słów_z_początkową_literą(lista_napisów, litera):
    return reduce(
        lambda akumulator, słowo: akumulator + [słowo] if (not akumulator or akumulator[-1] != słowo) and not słowo.startswith(litera) else akumulator,
        [słowo for napis in lista_napisów for słowo in napis.split()],
        []
    )

# ====================================================================
# 21. INDEKSY WYSTĄPIEŃ ELEMENTU
# ====================================================================

def indeksy(sekwencja, element):
    return map(fst, filter(eq(element) ** snd, enumerate(sekwencja)))

# ====================================================================
# 22. USUŃ_DUPLIKATY_SĄSIADUJĄCE
# ====================================================================

def usuń_duplikaty_sąsiadujące(lista):
    return reduce(lambda akumulator, element: akumulator if akumulator and akumulator[-1] == element else akumulator + [element], lista, [])

# ====================================================================
# PRZYKŁADOWE UŻYCIE
# ====================================================================

def main():
    print("=== Testy ===")
    
    # Cezar
    print("cezar('ABC', 3):", list(cezar("ABC", 3)))
    
    # Suma parzystych
    print("suma_parzystych([1,2,3,4,5,6]):", suma_parzystych([1,2,3,4,5,6]))
    
    # Euklides
    print("euklides([1,2,3], [4,5,6]):", euklides([1,2,3], [4,5,6]))
    
    # Maksimum
    print("maksimum([1,5,3,9,2]):", maksimum([1,5,3,9,2]))
    
    # Iloczyn rekurencyjny
    print("rekurencyjny_iloczyn([1,2,3,4]):", rekurencyjny_iloczyn([1,2,3,4]))
    
    # Sumowanie par
    print("sumuj_pary([(1,2), (3,4), (5,6)]):", sumuj_pary([(1,2), (3,4), (5,6)]))
    
    # Normalizacja wektora
    print("normalizuj_wektor([3,4]):", normalizuj_wektor([3,4]))
    
    # Łączenie krotek
    print("rekurencyjne_łączenie_krotek([(1,2), (3,4), (5,6)]):", rekurencyjne_łączenie_krotek([(1,2), (3,4), (5,6)]))
    
    # Usuwanie duplikatów sąsiadujących
    print("usuń_duplikaty_sąsiadujące([1,1,2,2,2,3,3,1]):", usuń_duplikaty_sąsiadujące([1,1,2,2,2,3,3,1]))
    
    # Indeksy
    print("list(indeksy([1,2,3,2,4,2], 2)):", list(indeksy([1,2,3,2,4,2], 2)))

if __name__ == "__main__":
    main()

# ====================================================================
# CHECKLISTA ZADAŃ
# ====================================================================

# zadanie 1. szyfr cezara  - cezar - na_kod - na_znak
# zadanie 2. dodaj_7 - dodaj_7
# zadanie 3. suma_parzystych - suma_parzystych
# zadanie 4. euklides - euklides
# zadanie 5. pomnóż_przez_3 - pomnóż_przez_3
# zadanie 6. filtruj_wartości_w_zakresie - filtruj_wartości
# zadanie 7. rekurencyjna_suma_krotek - rekurencyjna_suma_krotek
# zadanie 8. podziel_przez_3 - podziel_przez_3
# zadanie 9. maksimum - maksimum
# zadanie 10. rekurencyjny_iloczyn - rekurencyjny_iloczyn
# zadanie 11. usuń_samogłoski - usuń_samogłoski
# zadanie 12. podnieś_do_kwadratu - podnieś_do_kwadratu
# zadanie 13. rekurencyjna_średnia_i_wariancja - rekurencyjna_średnia_i_wariancja
# zadanie 14. filtruj_wektory - filtruj_wektory
# zadanie 15. sumuj_pary - sumuj_pary
# zadanie 16. odejmij_7 - odejmij_7
# zadanie 17. długość_wektora - długość_wektora
# zadanie 18. normalizuj_wektor - normalizuj_wektor
# zadanie 19. rekurencyjne_łączenie_krotek - rekurencyjne_łączenie_krotek
# zadanie 20. lista_napisów_bez_słów_z_początkową_literą - lista_napisów_bez_słów_z_początkową_literą
# zadanie 21. indeksy - indeksy
# zadanie 22. usuń_duplikaty_sąsiadujące - usuń_duplikaty_sąsiadujące
