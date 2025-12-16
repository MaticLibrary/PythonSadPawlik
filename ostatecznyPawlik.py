# Napisz funkcję sumuj_krotki, która:
# przyjmuje listę krotek 2-elementowych
# zwraca listę sum elementów każdej krotki
# MUSI używać list comprehension
# Przykład:
# sumuj_krotki([(1, 2), (3, 4), (5, 6)])
# zwraca [3, 7, 11]
def sumuj_krotki(lista_par):
    return [a[0] + a[1] for a in lista_par]
# #Polecenie:
# Napisz funkcję sumuj_napisy, która:
# przyjmuje dowolną liczbę par napisów
# każda para to krotka (imie, nazwisko)
# zwraca listę napisów połączonych spacją
def sumuj_napisy(*args):
    return [imie + " " + nazwisko for imie, nazwisko in args]

#Napisz funkcję filtruj, która:
# przyjmuje:
# funkcję jednoargumentową jako filtr
# listę danych
# zwraca listę elementów, dla których filtr zwraca True
def filtruj(filtr, lista):
    return [element for element in lista if filtr(element) == True]
#*args + sep – często myli)
# Polecenie:
# Napisz funkcję na_napis, która:
# przyjmuje dowolną liczbę argumentów
# posiada parametr sep z wartością domyślną "++"
# konwertuje wszystkie argumenty na str
# łączy je separatorem
def  na_napis(*args, sep = "++"):
    return sep.join([str(element) for element in args ])

# (funkcja typu all() – logika!)
# Polecenie:
# Napisz funkcję wszystkie, która:
# przyjmuje:
# funkcję jednoargumentową
# listę
# zwraca:
# False → jeśli choć jeden element zwróci False
# True → jeśli wszystkie zwrócą True
# True → jeśli lista jest pusta

def wszystkie(fun, lista):
    if not lista:
        return True
    if(all(fun(lista)) == True):
        return lista

# (przeszukiwanie listy – indeks pierwszego wystąpienia)
# Polecenie:
# Napisz funkcję znajdz_najmniejszy_indeks, która:
# przyjmuje listę liczb
# zwraca indeks wystąpienia najmniejszej liczby
# jeśli lista jest pusta → zwraca -1
# nie wolno używać operatorów arytmetycznych ani funkcji min()
def znajdz_najmniejszy_indeks(lista):
    if not lista:
        return -1
    min_index = -1
    min_value = None
    for index, element in enumerate(lista):
        if (min_value == None or min_value > element):
            min_value = element
            min_index = index
    return min_index

# generator – kwadraty)
# Polecenie:
# Napisz generator kwadraty, który:
# przyjmuje dowolną liczbę argumentów (*args)
# zwraca kolejno kwadraty elementów używając yield
def generator_kwadraty(*args):
    for arg in args:
        yield arg**2


# (funkcja typu any() – jakikolwiek)
# Polecenie:
# Napisz funkcję jakikolwiek, która:
# przyjmuje:
# funkcję jednoargumentową
# listę
# zwraca:
# True → jeśli przynajmniej jeden element spełnia warunek funkcji
# False → jeśli żaden element nie spełnia warunku lub lista jest pusta
def jakikolwiek(fun, lista):
    if not lista:
        return False
    for element in lista:
        if( fun(element) == True):
            return True
    return False
   #return [element for element in lista if fun(element) == True]


# klasa Wektor – magiczne metody)
# Polecenie:
# Napisz klasę Wektor, która:
# w konstruktorze przyjmuje listę liczb
# metoda __add__ dodaje elementy dwóch wektorów na przemian
# jeśli wektory mają różną długość → dopełnij krótszy zerami
# metoda __str__ zwraca reprezentację listy wektora
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
    
# Funkcja podaj_indeks – ostatnie wystąpienie elementu)
# Polecenie:
# Napisz funkcję podaj_indeks, która:
# przyjmuje listę liczb i szukaną wartość
# zwraca indeks ostatniego wystąpienia tej liczby
# jeśli liczby nie ma → zwraca -1
# nie używamy operatorów arytmetycznych ani range
def podaj_indeks(lista, wartosc):
    if not lista:
        return -1
    last_index = -1
    for index, element in enumerate(lista):
        if element == wartosc:
            last_index = index
    return last_index

# generator – zapis liczby słownie)
# Polecenie:
# Napisz generator zapis_slowny, który:
# przyjmuje liczbę
# używa słownika mapującego cyfry na słowa
# zwraca kolejno słowa odpowiadające cyfrom liczby
def generator(cyfraSlownie):
    mapa = {
        "0" : "zero",
        "1" : "jeden",
        "2" : "dwa" 
    }
    for element in str(cyfraSlownie):
        yield mapa[element]

# #Napisz klasy:
# Abstrakcyjna klasa Figura
# metoda abstrakcyjna obwod()
# statyczny licznik wszystkich figur (licznik), zwiększany w __init__
# Klasa Prostokat dziedzicząca po Figura
# konstruktor przyjmuje a i b
# metoda obwod() zwraca 2*(a+b)
# statyczny licznik prostokątów
from abc import ABC, abstractmethod
class Figura(ABC):  
    licznik = 0     
    def __init__(self):
        Figura.licznik += 1
    @abstractmethod
    def obwod(self):
        pass
class Prostokat(Figura):
    licznik_prostokatow = 0
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b
        Prostokat.licznik_prostokatow += 1
    def obwod(self):
        return 2*(self.a + self.b)
    @staticmethod
    def licznik_prostokatow():
        return Figura.licznik
# Funkcja sumująca napisy (pary)
# Polecenie:
# sumuj_napisy(("Jan","Nowak"), ("Adam","Kowalski"))
def sumuj_napisy(*pary):
    return [imie + " " + nazwisko for imie, nazwisko in pary]
# Funkcja podaj_numery – kontakty
# Polecenie:
# Napisz funkcję podaj_numery, która:
# przyjmuje:
# słownik kontaktów {(imie, nazwisko): numer_telefonu}
# nazwisko jako string
# zwraca listę numerów osób z podanym nazwiskiem
def podaj_numery(slownik, nazwisko):
    return [numer for (imie, nazw), numer in slownik.items() if nazw == nazwisko ]
#Funkcja sumuj_krotki – list comprehension
# Polecenie:
# przyjmuje listę krotek 2-elementowych
# zwraca listę sum elementów każdej krotki przez list comprehension
def sumuj_krotki(lista):
    return [x[0] + x[1] for x in lista]
#Funkcja znajdz_litere – indeks litery
# Polecenie:
# Napisz funkcję znajdz_litere, która:
# przyjmuje napis i literę
# zwraca indeks pierwszego wystąpienia litery w napisie
# jeśli litery nie ma → zwraca -1
def znajdz_litere(napis, litera):
    if not napis:
        return -1
    for index, wartosc in enumerate(napis):
        if wartosc == litera:
            return index
    return -1
#Napisz funkcję rzymski_na_arabski, która:
# przyjmuje napis reprezentujący liczbę rzymską
# używa słownika mapującego cyfry rzymskie na wartości arabskie
# algorytm:
# idąc od lewej do prawej, jeśli następny element większy → odejmij obecny
# w przeciwnym przypadku → dodaj obecny
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
#Klasa Wektor – magiczne metody
# Oczekiwane wcześniej rozwiązanie mamy już , więc następne zadanie:

# Funkcja generator_kwadraty – generator kwadratów
# Polecenie:
# Napisz generator generator_kwadraty, który:
# przyjmuje dowolną liczbę argumentów
# zwraca kolejno kwadraty elementów używając yield
def generator_kwadraty(*args):
    for arg in args:
        yield arg**2

#Funkcja jakikolwiek – sprawdzenie warunku
# Polecenie:
# Napisz funkcję jakikolwiek, która:
# przyjmuje funkcję jednoargumentową i listę
# zwraca True, jeśli chociaż jeden element listy spełnia warunek
# zwraca False, jeśli lista pusta lub żaden element nie spełnia warunku
def jakikolwiek(fun, lista):
    if not lista:
        return False
    for element in lista:
        if (fun(element) == True):
            return True
    return False


# Napisz funkcje sumuj_napisy ktora moze otrzymac dowolna liczbe par napisow (np (“Jan”,”Nowak”), (“Adam”,”Kowalski”)) i ma zwrocic liste polaczonych napisow, rozdzielonych spacja [“Jan Nowak”, “Adam Kowalski”]
def sumuj_napisy(*para):
    return [imie + " " + nazwisko for imie, nazwisko in para]
#funkcja która dostawala listę z krotkami które mają 2 wartości w sobie i zwracalo listę zrobioną za pomocą list comprehension która sumuje wartości w krotce
def sumuj_krotki(lista):
    return [x[0] + x[1] for x in lista]
    #return [a + b for a,b in zip(krotka1, krotka2)]
# lista krotek lista = ([1,2], [4,2])
def sumowanie_krotek(lista):
    new_lista = []
    for element in lista:
        suma = element[0] + element[1]
        new_lista.append(suma)
    return new_lista

#były klasy figura, prostokąt dziedziczy po figurze, kwadrat po prostokącie, wszystkie mają abstrakcyjna klase OD figury na obwod I figura ma statyczna co zlicza figury ile ich jest, wywolywane przez super().init
from abc import ABC, abstractmethod
class Figura(ABC):
    licznik = 0
    def __init__(self):
        Figura.licznik += 1
    @abstractmethod
    def obwod():
        pass
    @staticmethod
    def counter():
        return Figura.licznik
class Prostokat(Figura):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__()
    def obwod(self):
        return 2*(self.a + self.b)
class Kwadrat(Prostokat):
     def __init__(self, bok):
         super().__init__(bok, bok)

# Klasa a na init była podawane lista i funkcje _add  tam dodajemy na przemiennie elementy listy z dwóch obiektów klasy. I zwraca nowy wektor. Np. Obiekty nowy = wektor 1 + wektor 2. Potem metoda klasy do zaimplementowana str wypisujemy tam listę z wektoru czyli np print(wektor1) klasa wektor która dostaje listę, trzeba zrobić dodawanie (np innego wektora)- funkcja magiczna, trzeba zrobić wypisywanie wektora printem ( czyli str- magiczna),
class Wektor:
    def __init__(self,lista):
        self.lista = lista
    def __add__(self, other):
        new_wektor =  [a + b for a,b in zip(self.lista, other.lista)]
        return Wektor(new_wektor)
    def __str__(self):
        return str(self.lista)
    
## Napisz klasę Stopnie ze statyczną mapą (dictonary) zawierającą mapę cyfr na ich nazwy. W konstruktorze przyjmuje dowolny napis, funkcjonuje jak iterator, zwraca kolejne nieparzyste cyfry, kończy przy elementu niebędącym cyfrą.

class Stopnie:
    mapa = {
        '1' : 'jeden',
        '3' : 'trzy',
        '5' : 'piec',
        '7' : "siedem",
        '9' : 'dziewiec'
    }
    def __init__(self, napis):
        self.napis = napis
        self.element = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.element < len(self.napis):
            element = self.napis[self.element]
            self.element += 1
            if element.isdigit() and element in self.mapa:
                return self.mapa[element]
            elif not element.isdigit():
                raise StopIteration
        raise StopIteration

#było coś takiego że trzeba było zrobic funkcje która dostaje jakiś napis i literę, I ona ma znaleźć ta literę w tym napisie I podać potem ostatni (chyba) INDEKS gdzie znajduje się ta litera w tym napisie
def szukanie(napis, litera):
    if not napis:
        return -1
    for index, wartosc in enumerate(napis):
        if(litera == wartosc):
            return index
    return -1
#była funkcja jakikolwiek która miała funkcje jednoargumentowa jako parametr I listę, też jako parametr, I miała zwrócić true jeśli była w tej liście  jakaś liczba co była nieparzysty, a jak parzysta to false, a jak lista była pusta to też zwrocic false

def fun(element):
    if element %2 == 0:
        return True

def jakikolwiek(fun, lista):
    if not lista:
        return False
    for element in lista:
        if (fun(element) == True):
            return True
    return False

#Klasa a na init była podawane lista i funkcje _add  tam dodajemy na przemiennie elementy listy z dwóch obiektów klasy. I zwraca nowy wektor. Np. Obiekty nowy = wektor 1 + wektor 2. Potem metoda klasy do zaimplementowana str wypisujemy tam listę z wektoru czyli np print(wektor1) klasa wektor która dostaje listę, trzeba zrobić dodawanie (np innego wektora)- funkcja magiczna, trzeba zrobić wypisywanie wektora printem ( czyli str- magiczna),
class Wektor:
    def __init__(self, lista):
        self.lista = lista
    def __add__(self, other):
        wynik = [a + b for a,b in zip(self.lista, other.lista)]
        return Wektor(wynik)
    def __str__(self):
        return str(self.lista)
    

#był słownik który miał cyfry (wiecie 0 to zero itp) i trzeba było zrobić generator który zmieniał jakaś liczbe na jej zapis słowny, np 104 to jeden zero cztery
def generator(cyferki):
    mapa = {
        "zero" : "0",
        "jeden" : "1",
        "dwa" : "2",
        "trzy" : "3",
        "cztery" : "4",
        "piec" : "5"
    }
    for element in cyferki:
        if element.isdigit():
            yield element
        elif element in mapa:
            yield mapa[element]

#klasa Słownie ze statyczną mapą(dictionary) zawierającą mapy cyfr na ich nazwy w konstruktorze przyjmuje dowolny napis, funkcjionuje jak iterator, zwraca kolejno mapowane cyfry, konczy przy elementu nie bedacym cyfra
class Slownie:
    mapa = {
        "0": "zero",
        "1": "jeden",
        "2": "dwa",
        "3": "trzy",
        "4": "cztery",
        "5": "piec",
        "6": "szesc",
        "7": "siedem",
        "8": "osiem",
        "9": "dziewiec"
    }
    def __init__(self, napis):
        self.napis = napis
        self.pozycja = 0  
    def __iter__(self):
        return self
    def __next__(self):
        while self.pozycja < len(self.napis):
            element = self.napis[self.pozycja]
            self.pozycja += 1
            if element.isdigit():
                return self.mapa[element]
            else:
                raise StopIteration
        raise StopIteration
    

#     #Mamy liste kontaktow zapisanych w postaci słownika wpisow typu ( (imie,nazwisko): numer_telefonu) ) (Przykład takiego slownika to: (‘Jan', ‘Kowalski’):"123456789", (‘Adam', ‘Nowak’):"987654321". ([‘Adam', ‘Kowalski’): "600300900"))
# Napisz funkcję poďaj_ numery, która otrzymuje dwa argumenty: słownik z kontaktami i nazwisko, a zwraca listę numerów telefonu wszystkich osób o podanym (jako napis) nazwisku
def podaj_numery(slownik, nazwisko):
    return [numer for (imie, nazw), numer in slownik.items() if nazw == nazwisko]
#Napisz funkcje sumuj_napisy ktora moze otrzymac dowolna liczbe par napisow (np (“Jan”,”Nowak”), (“Adam”,”Kowalski”)) i ma zwrocic liste polaczonych napisow, rozdzielonych spacja [“Jan Nowak”, “Adam Kowalski”]
def sumuj_napisy(*para):
    return [imie + " " + nazwisko for imie, nazwisko in para]
#Napisz klase iteratora Kwadraty, ktorej “konstruktor” dostaje 1 lub 2 argumenty, 2 argumenty określają początek i koniec przedziału z ktorego brane sa liczby. Podanie jednego argumentu oznacza podanie konca argsu, a wartosc poczatku wynosi wowczas 1, iterator ma generowac kwadraty kolejnych wartosci calkowitych z podanego argsu (czyli np dla argsu (2,4) ma wygenerowac wartosci 4,9,16
class Kwadraty:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.end = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
        self.current = self.start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.end:
            wynik = self.current ** 2
            self.current += 1
            return wynik
        else:
            raise StopIteration
# Mamy liste kontaktow zapisanych w postaci słownika wpisow typu ( (imie,nazwisko): numer_telefonu) ) (Przykład takiego slownika to: (‘Jan', ‘Kowalski’):"123456789", (‘Adam', ‘Nowak’):"987654321". ([‘Adam', ‘Kowalski’): "600300900"))
# Napisz funkcję poďaj_ numery, która otrzymuje dwa argumenty: słownik z kontaktami i nazwisko, a zwraca listę numerów telefonu wszystkich osób o podanym (jako napis) nazwisku
def podaj_numery(slownik, nazwisko):
    return [numer for (imie, nazw), numer in slownik.items() if nazw == nazwisko]

##Napisz klase iteratora Kwadraty, ktorej “konstruktor” dostaje 1 lub 2 argumenty, 2 argumenty określają początek i koniec przedziału z ktorego brane sa liczby. Podanie jednego argumentu oznacza podanie konca argsu, a wartosc poczatku wynosi wowczas 1, iterator ma generowac kwadraty kolejnych wartosci calkowitych z podanego argsu (czyli np dla argsu (3)  (2,4) ma wygenerowac wartosci 4,9,16
class Kwadraty:
    def __init__(self, *args):
        if len(args) == 1:
            self.poczatek = 1
            self.koniec = args[0]
        elif len(args) == 2:
            self.poczatek = args[0]
            self.koniec = args[1]
        else:
            raise ValueError("Podaj 1 lub 2 argumenty")

        self.aktualny = self.poczatek

    def __iter__(self):
        return self

    def __next__(self):
        if self.aktualny > self.koniec:
            raise StopIteration

        wynik = self.aktualny ** 2
        self.aktualny += 1
        return wynik
#Funkcja podaj indeks zwraca najmniejszą liczbę z listy. Jeśli jest kilka wystąpień zwraca pierwszy indeks. Było to już nie wolno używać operatorów arytmetycznych ostatnie to zwrócenie indeksu najmniejszej wartości z listy
def najmniejszy_indeks(lista):
    if not lista:
        return -1
    min_value = None
    min_index = -1
    for index, element in enumerate(lista):
        if (min_value == None or min_value > element):
            min_value = element
            min_index = index
    return min_index

#Napisz funkcję znajdz_liczby_wspolne, która przyjmuje dwie listy liczb całkowitych. Funkcja ma znaleźć i zwrócić listę unikalnych liczb, które występują w obu listach.
def znajdz_liczby_wspolne(lista1, lista2):
    return list(set(lista1) & set(lista2))
## #Napisz klasy:
# Abstrakcyjna klasa Figura
# metoda abstrakcyjna obwod()
# statyczny licznik wszystkich figur (licznik), zwiększany w __init__
# Klasa Prostokat dziedzicząca po Figura
# konstruktor przyjmuje a i b
# metoda obwod() zwraca 2*(a+b)
# statyczny licznik prostokątów
from abc import ABC, abstractmethod
class Figura(ABC):
    counter = 0
    def __init__(self):
        Figura.counter += 1
    @abstractmethod
    def obwod(self):
        pass
class Prostokat(Figura):
    prostokatCounter = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()
        Prostokat.prostokatCounter += 1
    def obwod(self):
        return 2*(self.a + self.b)
#Klasa a na init była podawane lista i funkcje _add  tam dodajemy na przemiennie elementy listy z dwóch obiektów klasy. I zwraca nowy wektor. Np. Obiekty nowy = wektor 1 + wektor 2. Potem metoda klasy do zaimplementowana str wypisujemy tam listę z wektoru czyli np print(wektor1) klasa wektor która dostaje listę, trzeba zrobić dodawanie (np innego wektora)- funkcja magiczna, trzeba zrobić wypisywanie wektora printem ( czyli str- magiczna),
class Wektor:
    def __init__(self, lista):
        self.lista = lista

    def __add__(self, other):
        wynik = []
        # dodajemy elementy na przemian
        max_len = max(len(self.lista), len(other.lista))
        for i in range(max_len):
            if i < len(self.lista):
                wynik.append(self.lista[i])
            if i < len(other.lista):
                wynik.append(other.lista[i])
        return Wektor(wynik)

    def __str__(self):
        return str(self.lista)


### Napisz klasę Stopnie ze statyczną mapą (dictonary) zawierającą mapę cyfr na ich nazwy. W konstruktorze przyjmuje dowolny napis, funkcjonuje jak iterator, zwraca kolejne nieparzyste cyfry, kończy przy elementu niebędącym cyfrą.
class Stopnie:
    mapa = {
        '0' : "zero",
        '1' : "jeden",
        "2" : "dwa"
    }
    def __init__(self, napis):
        self.napis = napis
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.napis):
            znak = self.napis[self.index]
            self.index += 1

            if not znak.isdigit():
                raise StopIteration

            if znak in Stopnie.mapa:
                return Stopnie.mapa[znak]         

