#
from functools import reduce

# Funkcje i list comprehensions
#     Filtrowanie listy - Napisz funkcję filtruj, która przyjmuje funkcję filtrującą
#     i listę, zwraca elementy spełniające warunek
def filtrowanie(filtr, lista):
    return [wartosc for wartosc in lista if filtra(wartosc) == True]
#     Sumowanie krotek - Napisz funkcję sumuj_krotki, która przyjmuje listę krotek
#     i zwraca listę sum elementów
def sumowanieKrotek(krotka1, krotka2):
    return [a1 + a2 for a1, a2 in zip(krotka1,krotka2)]
#     Sprawdzanie warunku - Napisz funkcję wszystkie, która sprawdza czy wszystkie
#     elementy listy spełniają warunek
def SprawdzanieWarunku(lista, warunek):
    return [element for element in lista if element == warunek]
#     Generator kwadratów - Napisz generator kwadraty,
#     który zwraca kwadraty podanych argumentów
def generatorKwadratow(lista):
    return [wartosc*wartosc for wartosc in lista]


# Przetwarzanie napisów
#     Łączenie napisów - Napisz funkcję na_napis, która łączy dowolną
#     liczbę argumentów z separatorem
def na_napis(*args, sep =  "++"):
    return [ sep + arg + sep for arg in args]
#     Wyszukiwanie w tekście - Napisz funkcję znajdz_litere,
#     która znajduje indeks litery w napisie
def szukaj_w_tekscie(tekst, litera):
        if not tekst():
            return -1
        for index, znak in enumerate(tekst):
             if znak == litera:
                  return index
        return -1
#     Konwersja liczby na słowa - Napisz generator zapis_slowny,
#     który zamienia cyfry na ich nazwy
def generator(LiczbaStr):
     dict = {
          '0' : "zero",
          '1' : "jeden",
          '2' : "dwa",
          '3' : "trzy",
          '4' : "cztery",
          '5' : "piec"
    }
     for literka in LiczbaStr:
          if literka in dict(LiczbaStr):
               yield literka.items(LiczbaStr)

# POZIOM ŚREDNI
# Klasy i iteratory
#     Iterator Stopnie - Napisz klasę iteratora zwracającą
#     nazwy nieparzystych cyfr z napisu
class IteratorStopnie():
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.index = 0

    slownik = {
         '0' : "zero",
         '1' : 'jeden',
         '3' : "trzy",
         '5' : "piec",
         '7' : "siedem",
         '9' : "dziewiec"
    }

    def __iter__(self):
         return self
    
    def __next__(self):
        while self.index < len(self.wartosc):
            cyfra = self.wartosc[self.index]
            self.index += 1  # przesuwamy się dalej
            if cyfra in self.slownik:     # jest nieparzysta
                return self.slownik[cyfra]

        raise StopIteration
        return

#     Iterator Kwadraty - Napisz klasę iteratora generującą
#     kwadraty liczb z przedziału
class KwadratyIterator():
    def __init__(self):
          self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
         return liczba*liczba
#     Klasa Figura - Napisz abstrakcyjną klasę Figura
#     z metodą obwod() i licznikiem obiektów
import abc
from abc import ABC, abstractmethod

class Figura():
    counter = 0
    def __init__(self):
        Figura.counter += 1

    @abstractmethod
    def obwod(self):
        pass



#     Klasa Wektor - Napisz klasę Wektor z dodawaniem
#     i reprezentacją tekstową
class Wektor():
    def __init__(self, wektor1, wektor2):
        self.wektor1 = wektor1  
        self.wektor2 = wektor2  
    
    def wypisz(self):
        return f"({self.wektor1}, {self.wektor2})"
    
    def __add__(self, other):  
        return Wektor(
            self.wektor1 + other.wektor1,  
            self.wektor2 + other.wektor2
        )


# Zadanie 1: Parzyste Filtry
# Napisz funkcję, która otrzymuje listę list liczb. Zwróć tylko te podlisty, które zawierają przynajmniej 
# jedną liczbę podzielną przez 3. Użyj filter i any
def ParzysteFiltry(listaListLiczb):
    return list(filter(lambda podlista: any(x % 3 == 0 for x in podlista),listaListLiczb))
        #   lista  filtr(funckja dla listy: warunek dla elementu listy w lista) glowna lista

# ZADANIE 2: Suma Nieparzystych Indeksów
# Dla listy liczb zwróć sumę elementów na nieparzystych indeksach (1, 3, 5...). 
# Użyj enumerate, filter i reduce.
# def SumaNieparzystychIndeksow(lista):
#     return list(filter(lambda elementListy: ))


# nums = [1, 2, 3, 4, 5]
# list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
# list(map(lambda x,y: x+y, [1,2,3], [4,5,6]))  # [5, 7, 9]
# Zadanie: Wybierz tylko liczby parzyste z listy
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)  # [2, 4, 6, 8, 10]
# filter(warunek, kolekcja) → zwraca tylko elementy gdzie warunek = True
# lambda x: x % 2 == 0 → funkcja sprawdzająca parzystość
# Twoje zadanie: Napisz funkcję, która wybiera tylko liczby większe od 5.
# python
liczby = [3, 7, 1, 9, 4, 6]
def wiekszeod5(liczby):
    return list(filter(lambda cyfra: cyfra > 5 , liczby))

# Twoje zadanie: Napisz funkcję, która dodaje 10 do każdej liczby.
# python
liczby = [5, 15, 25]
def dodawanieWartosci(lista):
    return list(map(lambda cyferka: cyferka + 10, lista))

# Dla listy [3, 7, 2, 8, 5] użyj filter do wybrania liczb > 4
def wiekszeOd4(lista):
    return list(filter(lambda cyfra: cyfra > 4, lista))

# Dla listy [10, 20, 30] użyj map do dodania 5 do każdej liczby
def mapdodawaniewartosci5(lista):
    return list(map(lambda cyfra: cyfra + 5, lista))

#Dla listy [1, 2, 3, 4] użyj reduce do mnożenia
def mnozenieWartosciReduce(lista):
    return reduce(lambda a, b: a * b, lista)  # BRAK list()! reduce zwraca wartość


# Użyj filter i map: dla [1, 2, 3, 4, 5] wybierz parzyste i podnieś do 3 potęgi
def filtermaParzystaPow(lista):
    return list(filter(map(lambda x: x % 2 == 0, x**3, lista)))

# Użyj reduce do sumowania: dla [1, 2, 3, 4] zwróć sumę
reduce_result = reduce(lambda a,b: a+b, [1,2,3,4])  # 10 ← od razu wartość

#  Użyj filter i map: dla [1, 2, 3, 4, 5] wybierz parzyste i podnieś do 3 potęgi
def mapifilter(lista):
    def filtr(lista):
        return list(filter(lambda element: element % 2 == 0, lista))
    return list(map(lambda element: element**3, filtr(lista)))
