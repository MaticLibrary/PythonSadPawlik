#                           Grupa I
# Zadanie 1

#Napisz funkcję filtruj, która przyjmuje funkcję jednoargumentową jako filtr i listę danych, zwraca listę z wartościami dla których filtr zwraca True.

def filtruj(filtr, dane):
    return [x for x in dane if filtr(x)]
  
  
# Zadanie 2

#Napisz funkcję na_napis, która przechowuje dowolną liczbę argumentów i separator z wartością domyślną "++", konwertuje wszystko na string i łączy.

def na_napis(*args, sep = "++"):
    return sep.join(str(x) for x in range args)


# Zadanie 3

# Napisz funkcję znajdz_wartosc, która zwraca indeks szukanej liczby z podanej listy, -1 jeżeli nie znajdzie. Zakaz używania arytmetyki oraz range.

def znajdz_wartosc(text, wartosc):
    for index, char in enumerate(text):
        if (char == wartosc):
            return index
        else:
            return -1
          
# Zadanie 4

# Napisz funkcję sumuj_krotki, która przyjmuje listę krotek i zwraca listę sum elementów krotek przez List Comprehension.

def summuj_krotki(krotka1, krotka2):
    return [a + b for a, b in zip(krotka1, krotka2)]


# Zadanie 5

# Napisz klasę Stopnie ze statyczną mapą (dict) zawierającą mapę cyfr na ich nazwy. W konstruktorze przyjmuje dowolny napis, funkcjonuje jak iterator, zwraca kolejne nieparzyste cyfry, kończy przy znaku niebędącym cyfrą.

class Stopnie:
     mapa = {
        '0': 'zero',
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'piec',
        '6': 'szesc',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewiec'
     }
     def __init__(self, napis):
         self.napis = napis
         self.pozycja = 0
     def __iter__(self):
        return self
     def __next__(self):
         while self.pozycja < len(self.napis):
             znak = self.napis[self.pozycja]
             self.pozycja += 1
             if znak in self.mapa and int(znak) % 2 != 0:
                 return self.mapa[znak]
         raise StopAsyncIteration


#####                                                                         GRUPA II

# Zadanie 1:
#Napisz klasę iterator Kwadraty, której konstruktor dostaje 1 lub 2 argumenty. 2 argumenty określają początek i koniec przedziału, z którego brane są liczby. Podanie jednego argumentu oznacza podanie końca przedziału a wartość początkowa wynosi wówczas 1. Iterator ma generować kwadraty kolejnych wartości całkowitych z podanego przedziału.
class Kwadraty:
    def __init__(self, *args):
        if( len(args) == 1):
            self.start = 1
            self.koniec = args[0]
        else:
            self.start, self.koniec = args
            self.aktualny = self.start
    def __iter__(self):
        return self
    def __next__(self):
        if self.aktualny > self.koniec:
            raise StopIteration
        kwadrat = self.aktualny ** 2
        self.aktualny += 1
        return kwadrat

  
#Zadanie 2
#Napisz funkcję sumuj_napisy, która może otrzymać dowolną liczbę par napisów np. (("Jan", "Nowak"), ("Adam", "Kowalski")) ma zwrócić listę połączonych napisów, rozdzielonych spacją ["Jan Nowak", "Adam Kowalski"]
def sumuj_napisy(*pary):
    return [f"{imie} {nazwisko}" for imie, nazwisko in pary]

# Zadanie 3
# Mamy listę kontaktów zapisanych w postaci słownika wpisów typu {(imie, nazwisko): numer_telefonu}. Napisz funkcję podaj_numery, która otrzymuje dwa argumenty: słownik z kontaktami i nazwisko, a zwraca listę numerów telefonu wszystkich osób o podanym nazwisku

def podaj_numery(kontakty, nazwisko):
    return [numer for (imie, nazw), numer in kontakty.items() if nazw == nazwisko]

# Zadanie 4
# Napisz funkcję podaj_indeksy, która w podanej jako pierwszy parametr liście liczb znajdzie i zwróci położenie (indeks) ostatniego wystąpienia liczby podanej jako drugi parametr. W wypadku, kiedy takiej liczby nie będzie w liście funkcja ma zwrócić -1. Indeksy liczymy od 0. Należy użyć pętli for BEZ range. Ponadto w programie nie może wystąpić żadne działanie arytmetyczne.
def podaj_indeksy(lista, wartosc):
    last_index = -1
    index = 0
    for element in lista:
        last_index = index
        index += 1
    return last_index

#                                                                     Grupa III   najmniejsz precyzyjne informacje dotyczace polcenia
# Zadanie I
#Napisz generator, który zmienia liczbę na jej zapis słowny używając słownika mapującego cyfry na ich nazwy (np. '0': 'zero'). Dla liczby 104 generator powinien zwrócić: 'jeden', 'zero', 'cztery'.

def zapis_slowny(liczba):
    mapa = {
        '0' : 'zero',
        '1' : 'jeden',
        '2' : 'dwa',
        '3' : 'trzy',
        '4' : 'cztery',
        '5' : 'piec',
        '6' : 'szesc',
        '7' : 'siedem',
        '8' : 'osiem',
        '9' : 'dziewiec'
    }
    for cyfra in str(liczba):
        yield mapa[cyfra]

# Zadanie 2
#Napisz abstrakcyjną klasę Figura z metodą obwod(). Następnie napisz klasę Prostokat dziedziczącą po Figura. Wszystkie klasy mają mieć statyczny licznik zliczający ile obiektów każdej figury zostało utworzonych (wywoływany przez super().__init__()).

from abc import ABC, abstractmethod
class Figura(ABC):
    licznik = 0
    def __init__(self):
        super().__init__()
        Figura.licznik += 1

    @abstractmethod
    def obwod(self):
        pass
class Prostokat(Figura):
    licznik = 0
    def __init__(self, a, b):
        super().__init__()
        Prostokat.licznik += 1
        self.a = a
        self.b = b
    def obwod(self):
        return 2 * (self.a + self.b)
    
# Zadanie 3
#Napisz funkcję, która dostaje listę z krotkami które mają 2 wartości w sobie i zwraca listę zrobioną za pomocą list comprehension która sumuje wartości w krotce.
def sumuj_krotke(krotki):
    return [k[0] + k[1] for k in krotki]

# Zdanie 4
# Napisz funkcję, która dostaje napis i literę, ma znaleźć tę literę w napisie i podać indeks gdzie znajduje się ta litera w napisie.
def znajdz_litere(napis, litera):
    for indeks, znak in enumerate(napis):
        if znak == litera:
            return indeks
        else:
            return -1


        
#                                                                             Grupa IV  tutaj jednak najmniej dokladne informacje dotyczace polecenia 
# Zadanie 1
#Napisz funkcję rzymski_na_arabski, która przyjmuje napis reprezentujący liczbę w systemie rzymskim i zwraca jej wartość w systemie arabskim. Użyj słownika mapującego cyfry rzymskie na ich wartości. Algorytm: przechodząc przez znaki od lewej do prawej, jeśli następny znak ma większą wartość niż obecny, to odejmujemy obecną wartość, w przeciwnym przypadku dodajemy.
def rzymski_na_arabski(napis):
    slownik = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    wynik = 0
    for i in range(len(napis)):
        if i + 1 < len(napis) and slownik[napis[i]] < slownik[napis[i + 1]]:
            wynik -= slownik[napis[i]]
        else:
            wynik += slownik[napis[i]]
    return wynik

# Zadanie 2
#Napisz klasę Wektor, która w konstruktorze przyjmuje listę liczb. Zaimplementuj metodę __add__ dodającą na przemian elementy z dwóch wektorów (jeśli wektory są różnej długości, dopełnij krótszy zerami). Zaimplementuj również metodę __str__ zwracającą reprezentację wektora jako listy.

class Wektor:
    def __init__(self, lista):
        self.lista = lista
    
    def __add__(self, other):
        wynik = []
        max_len = max(len(self.lista), len(other.lista))
        
        for i in range(max_len):
            val1 = self.lista[i] if i < len(self.lista) else 0
            val2 = other.lista[i] if i < len(other.lista) else 0
            wynik.append(val1 + val2)
        
        return Wektor(wynik)
    
    def __str__(self):
        return str(self.lista)
    
# Zadanie 3
#Napisz funkcję znajdz_najmniejszy_indeks, która zwraca indeks pierwszej wystąpionej najmniejszej liczby w liście. Jeśli lista jest pusta, zwraca -1. Nie wolno używać operatorów arytmetycznych ani funkcji min(

def znajdz_najmniejszy_indeks(lista):
    if not lista:
        return -1
    
    min_index = 0
    min_value = lista[0]
    
    for i, element in enumerate(lista):
        if element < min_value:
            min_value = element
            min_index = i
    
    return min_index

# Zadanie 4
#Napisz generator kwadraty, który przyjmuje dowolną liczbę argumentów i zwraca kwadraty tych elementów używając yield.

def kwadraty(*args):
    for x in args:
        yield x ** 2

# Zadanie 5
# Napisz funkcję wszystkie, która przyjmuje funkcję sprawdzającą i listę. Jeśli funkcja sprawdzająca zwróci False dla choć jednego elementu, cała funkcja zwraca False. Jeśli wszystkie elementy spełniają warunek lub lista jest pusta, zwraca True.

def wszystkie(funkcja, lista):
    for element in lista:
        if not funkcja(element):
            return False
    return True




# listopad  19 2025 
