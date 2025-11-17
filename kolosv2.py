#Tutaj beda wszystkie funkcje z podstawy
#Niektóre zadania to programy w main aby mudz napisac wszystko co sie da  bede sie staral umieszczac je w funkcjach
# dla lepszego zrozmienia bede to tlumaczyl od zera
import math
from abc import ABC, abstractmethod
from random import random
from time import perf_counter


#Zadanie szukanie A
def find_a(input_of_string):
    char_counter=0 # zmienna pod ktora bedziemy przechwywac wysapienia znakow
    for char in input_of_string: # petla ktora mowi przejdz przez wszystkie znaki w inputcie gdyz w tym zadniu mamy znalesc a w znaku z klawiatury
        if char=='a' or char=='A': # warunek ktory sprawdza czy znak jest rowny a albo A
            char_counter+=1 #za kadzym razem gdy znak wystąpi zliczamy znaki
        return char_counter # zwracamy wynik

#Szukanie 'A' - indeksy
def find_a_index(input_of_string):
    # enumerate tworzy nam z inputu pary index i znak np znak abc  (0,a) dlatego mamy w for dwie dane index i znak
    #warunek gdy znajdzie a lub A jak wczesniej printuje pierwszy element pary czyli nasz szukany index
    for index,char in enumerate(input_of_string):
        if char=='a' or char=='A':
            print(f"Znaleziono 'a' lub 'A' na indeksie: {index}")

#Zgaduj zgadula
def play_guessing_game():
    number_to_guess = random.randint(1, 10) #tutaj generujemy losowa liczbe z zakresu od 1,10
    chances = 3 #mozliwe proby zgadniecia
    guess_counter = 0 #zmienna liczaca nasza ilosc prob

    while guess_counter < chances: #warunek ktory dopunki ilosc naszych bedzie mniesza od wszystkich prob dopuszca nasz do gry
        guess_counter += 1 # za kazdym razem gdy nie zgadniemy ilosc naszym prob sie zwieksza gdy dojdzie do 3 aktywuje sie while
        my_guess = int(input('Please Enter your Guess: ')) # input do wprowadzenia liczby

        if my_guess == number_to_guess: #jezeli nasz input jest rowny wylosowanej liczbie zadliśmy
            print('Udało się! Zgadłeś liczbę', number_to_guess)
            break
        elif my_guess < number_to_guess: #jezeli nasz input jest mnieszy niz liczba ktora chcemy zgadąc print daje podpowiedz
            print('Twoja liczba jest większa.')
        elif my_guess > number_to_guess: #jezeli nasz input jest wiekszy niz liczba ktora chcemy zgadąc print daje podpowiedz
            print('Twoja liczba jest mniejsza.')
    else:
        print('Oj, niestety. Szukana liczba to', number_to_guess, 'Powodzenia!') #jezeli nie trafilsmy 3 razy odpala sie while ktory konczy gre


#Teraz ważniesze rzeczy na kolosa Temat kolekcje

#Suma krotek -to bylo na naszej grupie kolosa
def sum_tuples(tuple_list):
    result=[] #pusta lista wynikowa
    # petla ktora iteruje przez wszystkie krotki w liscie tuple_list dlaczego a,b bo w ten sposob iterujemy przez 2 elementowe krotki
    for a,b in tuple_list:
        result.append(a+b) # do listy wynikowej dodajemy appendem do siebie pierwszy i 2 element krotki
    return result # zwracamy liste wynikowa

#Lata przestępne
def leap_year(year):
    rok_poczatkowy = int(input("Podaj rok początkowy: ")) #input roku poczatkowego
    rok_koncowy = int(input("Podaj rok końcowy: ")) # input roku koncowego

    lata_przestepne = [rok for rok in range(rok_poczatkowy, rok_koncowy)
                       if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)]

    # tutaj mamy doczynienia z list comprehension ktora tworzy nam nowa liste lata przestepne
    # skladnia list comprehension po pierwsze element ktory chcemy utorzyc pozniej for ktory przechodzi i tworzy elementy
    # w tym przyadku w rangu ktory podamy zwykle podajemy nowa liste a nastepne moze byc warunek if ktory jest kryterium
    # jakie elementy chcemy w liscie miec w tym przadku lata przestepne
    print("Lata przestępne w podanym przedziale:", lata_przestepne)

# Cyfry słownie

def zamien_na_slowne(liczba_str):
    #mamy tu przypadek uzycia slownika kazdy jego element sklada sie z klucza i wartosci
    liczebniki = {
        '0': 'zero',
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć'}
    wynik = "" # zmienna wynikowa

    for znak in liczba_str: # petla ktora iteruje przez wszystkie znaki w stringu ktory podamy

        if znak.isdigit(): # warunek ktory korzysta z metody isdigit ktora sprawdza czy znak jest cyfra
            wynik += liczebniki[znak] + " "  # jezeli znak jest cyfra do wyniku dodajemy do niego wartosc z slownika

    return wynik.strip() # zwracamy wynik z strip() ktory usuwa spacje na poczatku i na koncu

#To zadnie u nas bylo na kolosie ale Cyfry słownie jako generator

def zamien_na_slowne_generator(liczba_str):
    liczebniki = {
        '0': 'zero',
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć'}
    for znak in liczba_str: # petla ktora iteruje przez wszystkie znaki w stringu ktory podamy
        if znak.isdigit(): # warunek ktory korzysta z metody isdigit ktora sprawdza czy znak jest cyfra
            yield liczebniki[znak]   # Korzystamy z generatora, aby zwrócić odpowiednik słowny cyfry w kolejnych przejsciach peetli


# Rzymskie - tego zadania raczej w zadnej grupie nie bylo jest za trudne na kolosa
def roman_to_int(s):
    # slownik ktory pod kluczami cyfr rzymskich podajemy ich wartosci w liczbie dziesietnej
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
        'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    i = 0 # indeks
    num = 0 # zmienna z wynikiem

    # Pętla iterująca po ciągu
    while i < len(s) - 1:
        # Sprawdzenie, czy bieżący i następny znak są kombinacją rzymską
        if s[i:i+2] in roman:
            num += roman[s[i:i+2]]  # Dodanie wartości kombinacji
            i += 2  # Przejście o dwa znaki dalej
        else:
            num += roman[s[i]]  # Dodanie wartości pojedynczego znaku
            i += 1  # Przejście o jeden znak dalej

    # Dodanie wartości ostatniego znaku
    num += roman[s[-1]]

    return num

# Spis kontaktów
def contact_list():
    kontakty = {
        #Tu mamy slownik ktory jako klucz wykorzystuje kortke z imieniem i nazwiskiem a wartosc to numer telefonu
        ('Jan', 'Kowalski'): "123456789",
        ('Adam', 'Nowak'): "987654321",
        ('Adam', 'Kowalski'): "600300900"}

    print(kontakty["Adam", "Kowalski"]) # to byla piersza czesc zadania wystlenie numeru o nazwisku Adam Kowalski

    # petla for iteruje przez kolejno (imie,nazwisko) czyli krotke ktora jest kluczem w slowniku
    #oraz number gdyz jego szukamy dalsza czesc kodu to kontakty.items metoda .items pozwala nam iterowac przez klucze i wartosci na raz
    # uzywane tylko w slownikach a warunek if sprawdza czy nazwisko jest rowne Kowalski i jesli tak wypisuje numer
    for (imie, nazwisko), numer in kontakty.items():

        if nazwisko == "Kowalski":
            print(f"{numer}")

# Wspolne elementy
def common_elements(lst_one,lst_two):
    # w tym zadaniu wykorzystujemy funkcje set ktora tworzy nam zbior , zbior to kolekcja unikalnych elementow
    # np jezeli mamy liste [1,1,2,2,3,3] to set bedzie [1,2,3]
    a_set = set(lst_one)
    b_set = set(lst_two)
    # pod zmienna a_set przypisujemy liste pierwsza ktora jest zmodyfikowana przez set np tu damy liste [1, 2, 3, 4, 4] po set [1, 2, 3, 4]
    # pod zmienna b_set przypisujemy liste druga ktora jest zmodyfikowana przez set np tu damy liste [3, 4, 5, 6, 6] po set [3, 4, 5, 6]
    common = a_set & b_set
    # pod zmienna common przypisujemy zbior ktory bedzie zawieral wspolne elementy z obu zbiorow operator & wyciaga
    # elementy wspolne z obu zbiorow
    return common

#Wariancja
def average_and_variation(list_of_numbers):
    n=len(list_of_numbers) # liczba elementow w liscie
    average=0 # zmienna do obliczenia sredniej ktora na poczatku jest zerowa
    for number in list_of_numbers: # petla przechodzi po liscie
        average=average+number # dodaje elementy do sredniej
    average=average/n # na koniec dzieli wynik przez przez liczbe elementow



    sum_of_squares = 0 # zmienna do obliczenia wariancji
    for number in list_of_numbers: # petla przechodzi po liscie
        sum_of_squares += (number - average) ** 2 # dodaje do sumy kwadraty roznicy elementow od sredniej

    variance = sum_of_squares / n # na koniec dzieli wynik przez przez liczbe elementow
    return average, variance

# Pola Figur
def oblicz_pola(*figury):
    pola = {'koło': [], 'kwadrat': [], 'prostokąt': [], 'trójkąt': []} # slownik ktory sklada sie z kluczy i wartosci

    for figura in figury: # petla ktora przez przez figury
        nazwa, dane = figura[0], figura[1:] # pod zmienna nazwa przypisujemy nazwe figury a pod zmienna dane przypisujemy dane figury

        if nazwa == 'koło':
            promien = dane[0] # pod zmienna promien przypisujemy pierwszy element ktory jest promienem
            pole = math.pi * promien ** 2 # obliczanie pola
            pola['koło'].append(pole) # do listy wynikowej dodajemy appendem do siebie pierwszy i 2 element krotki

        elif nazwa == 'kwadrat':
            bok = dane[0] # pod zmienna bok przypisujemy pierwszy element ktory jest bokiem
            pole = bok ** 2 # obliczanie pola
            pola['kwadrat'].append(pole) # do listy wynikowej dodajemy appendem do siebie pierwszy i 2 element krotki

        elif nazwa == 'prostokąt':
            bok1, bok2 = dane # pod zmienna bok1 przypisujemy pierwszy i drugi element ktory jest bokami
            pole = bok1 * bok2 # obliczanie pola
            pola['prostokąt'].append(pole) # do listy wynikowej dodajemy appendem do siebie pierwszy i 2 element krotki

        elif nazwa == 'trójkąt':
            podstawa, wysokosc = dane # pod zmienna podstawa przypisujemy pierwszy i drugi element ktory jest bokami
            pole = 0.5 * podstawa * wysokosc # obliczanie pola
            pola['trójkąt'].append(pole) # do listy wynikowej dodajemy appendem do siebie pierwszy i 2 element krotki

    return pola

# Pochodna
def derivative(f, x, h=0.0001): # funkcja do obliczenia pochodnej funkcji
    return (f(x + h) - f(x)) / h # obliczanie pochodnej na podstawie wzoru z zadaniu


def square(x): # funkcja do obliczenia kwadratu
    return x ** 2 # obliczanie kwadratu


sin_derivative_at_1 = derivative(math.sin, 1) #
sin_derivative_at_0 = derivative(math.sin, 0)


square_derivative_at_1 = derivative(square, 1, h=0.00001) #tutaj przyklad uzycia funkcji w funkcji podobne bylo na kolosie

#Dekorator
# Polega na tym ze w fukcji counter_time umieszczamy funkcje ktora chcemy dekorowac zawsze w
# pierwzym defie musi byc func gdyz to nazwa uniwersalna bo zawsze dekorujemy funkcje a nie wiemy jaka wiec dajemy by defult
# func  , nastepy jest wrapper *args i **kwargs nie wiemy ile argumentow ma funkcja ale zawsze bedzie to *args i **kwargs czyli
# dowolna ilosc argumentow w niej kolejno start liczenia czasu pozniej result wywoluje funkcje func(czyli jakas nasza) pozniej
# konczy liczyc czas i daje print z tym czasem a nastepnie zwraca wynik
def counter_time(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Czas wykonywania funkcji {func.__name__}: {end_time - start_time} sekund")
        return result
    return wrapper

#Figury


# Figury to bedzie na sto procent dziedziczenie w sensie
class Ksztalt(ABC):
    # klasa bazowa dla wszystkich ksztaltow, zawiera wspólne cechy, takie jak nazwa kształtu
    def __init__(self, name):
        # prywatny atrybut przechowujący nazwę kształtu ,zawsze zaczyna sie od podkreslenia __
        self.__name = name

    def get_name(self):
        # Zwraca nazwę kształtu
        return self.__name

    @abstractmethod
    def pole(self):
        # metoda abstrakcyjna do obliczania pola kształtu
        # musi być zaimplementowana w każdej klasie pochodnej
        pass # pusta metoda

# Klasa Kolo dziedziczy po Ksztalt
class Kolo(Ksztalt):
    # Klasa reprezentująca koło
    def __init__(self, name, promien):
        # Wywołanie konstruktora klasy bazowej inaczej jezeli chcemy dziedziczyc po innej klasie to super().__init__(name)
        # pobierze  name z klasy bazowej
        super().__init__(name)
        # Promien kola
        self.promien = promien

    def pole(self):
        # Oblicza pole kola
        return math.pi * self.promien ** 2

# Klasa Trojkat dziedziczy po Ksztalt
class Trojkat(Ksztalt):
    # klasa reprezentująca trojkąt
    def __init__(self, name, bok_a, bok_b, bok_c):
        # Wywołanie konstruktora klasy bazowej
        super().__init__(name)
        # bok a trojkąta
        self.bok_a = bok_a
        # bok b trojkąta
        self.bok_b = bok_b
        # bok c trojkąta
        self.bok_c = bok_c

    def pole(self):
        # Oblicza pole trójkąta
        return self.bok_a * self.bok_b ** 2

# Klasa Prostokat dziedziczy po Ksztalt
class Prostokat(Ksztalt):
    # Klasa reprezentująca prostokąt
    def __init__(self, name, bok_a, bok_b):
        # Wywołanie konstruktora klasy bazowej
        super().__init__(name)
        # dlugość pierwszego boku prostokata
        self.bok_a = bok_a
        # dlugość drugiego boku prostokata
        self.bok_b = bok_b

    def pole(self):
        # oblicza pole prostokata
        return self.bok_a * self.bok_b

# Klasa Kwadrat dziedziczy po Prostokat
class Kwadrat(Prostokat):
    # klasa reprezentująca kwadrat, będący szczegolnym przypadkiem prostokata
    def __init__(self, name, bok_a):
        # wywołanie konstruktora prostokat z tą samą dlugością bokow
        super().__init__(name, bok_a, bok_a)

# Klasa Trojkat_rownoboczny dziedziczy po Trojkat
class Trojkat_rownoboczny(Trojkat):
    # klasa reprezentująca trojkąt rownoboczny, będący szczególnym przypadkiem trojkąta
    def __init__(self, name, bok_a):
        # wywolanie konstruktora trojkat, gdzie wszystkie boki są rowne
        super().__init__(name, bok_a, bok_a, bok_a)


#Ulamek

class ulamek_niewlasciwy:
    # klasa reprezentujaca ulamek niewlasciwy

    liczba_instancji = 0  # licznik instancji klasy

    def __init__(self, licznik, mianownik):
        # konstruktor przyjmuje licznik i mianownik
        self.licznik = licznik
        self.mianownik = mianownik

        ulamek_niewlasciwy.liczba_instancji += 1  # zwiekszenie licznika instancji

    @classmethod
    def fromdecimal(cls, liczba_dziesietna):
        # metoda tworzy ulamek z liczby dziesietnej
        mianownik = 1  # ustawiamy poczatkowy mianownik
        while liczba_dziesietna % 1 != 0:  # dopoki liczba dziesietna ma czesc ulamkowa
            liczba_dziesietna *= 10  # przesuwamy przecinek w prawo
            mianownik *= 10  # zwiekszamy mianownik odpowiednio
        instancja = cls(int(liczba_dziesietna), mianownik)  # tworzymy obiekt klasy
        return instancja

    def reduction(self):
        # metoda upraszcza ulamek przez znalezienie najwiekszego wspolnego dzielnika (nwd)
        gcd = math.gcd(self.licznik, self.mianownik)  # obliczamy nwd
        self.licznik //= gcd  # dzielimy licznik przez nwd
        self.mianownik //= gcd  # dzielimy mianownik przez nwd
        return self

    def _nww(self, other):
        # metoda oblicza najmniejsza wspolna wielokrotnosc (nww) mianownikow
        return (self.mianownik * other.mianownik) // math.gcd(self.mianownik, other.mianownik)

    def __add__(self, other):
        # metoda definiuje dodawanie ulamkow
        nww = self._nww(other)  # obliczamy nww
        licznik = self.licznik * (nww // self.mianownik) + other.licznik * (nww // other.mianownik)
        return ulamek_niewlasciwy(licznik, nww).reduction()  # zwracamy wynik po uproszczeniu

    def __sub__(self, other):
        # metoda definiuje odejmowanie ulamkow
        nww = self._nww(other)  # obliczamy nww
        licznik = self.licznik * (nww // self.mianownik) - other.licznik * (nww // other.mianownik)
        return ulamek_niewlasciwy(licznik, nww).reduction()  # zwracamy wynik po uproszczeniu

    def __mul__(self, other):
        # metoda definiuje mnozenie ulamkow
        licznik = self.licznik * other.licznik  # mnozymy liczniki
        mianownik = self.mianownik * other.mianownik  # mnozymy mianowniki
        return ulamek_niewlasciwy(licznik, mianownik).reduction()  # zwracamy wynik po uproszczeniu

    def __truediv__(self, other):
        # metoda definiuje dzielenie ulamkow
        licznik = self.licznik * other.mianownik  # licznik mnozymy przez mianownik drugiego ulamka
        mianownik = self.mianownik * other.licznik  # mianownik mnozymy przez licznik drugiego ulamka
        return ulamek_niewlasciwy(licznik, mianownik).reduction()  # zwracamy wynik po uproszczeniu

    def __str__(self):
        # metoda zwraca reprezentacje ulamka w formie tekstowej
        return f"{self.licznik}/{self.mianownik}"

    @classmethod
    def liczba_obiektow(cls):
        # metoda zwraca liczbe utworzonych instancji klasy
        return cls.liczba_instancji











