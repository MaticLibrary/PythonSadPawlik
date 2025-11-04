#  Klasa Kształt ma być klasą abstrakcyjną i zawierać ukryty (prywatny) atrybut z
# nazwą figury dostępny poprzez getter (należy wykorzystać @property). Atrybut ten należy
# wypełniać w __init__ na podstawie parametru. Ponadto ma zawierać abstrakcyjną metodę pole.
# Następnie należy stworzyć klasy pochodne od klasy Kształt:
# - Koło(nazwa, promień)
# - Trójkąt(nazwa, bok_a, bok_b, bok_c)
# - Prostokąt(nazwa, bok_a, bok_b)
# Każda z figur ma umieć wyliczyć swoje pole za pomocą metody pole
# W kolejnym kroku należy dla Prostokąta i Trójkata utworzyć ich klasy pochodne opisujące ich
# wersje foremne (czyli kwadrat i trójkąt równoboczny). Mają one zawierać jedynie odpowiednie
# konstruktory (żadnych innych metod ani atrybutów).
# W main należy stworzyć listę figur zawierającą przykładowe obiekty każdej z klas pochodnych i w
# pętli wypisać nazwy figur oraz ich pola

import math
from abc import ABC, abstractmethod

class Ksztalt(ABC):  ## ABC — oznacza, że Ksztalt to klasa abstrakcyjna.
    def __init__(self, nazwa: str):
        self.__nazwa = nazwa
    @property   # @property — getter, dzięki któremu możemy odczytywać nazwę np. figura.nazwa.
    def nazwa(self):
        return self.__nazwa     ## __nazwa — prywatny atrybut (dostępny tylko wewnątrz klasy).
    @abstractmethod ## @abstractmethod — metoda, którą muszą zaimplementować wszystkie klasy dziedziczące.
    def pole(self):
        pass

class Kolo(Ksztalt):
    def __init__(self, nazwa, promien):
        super().__init__(nazwa)
        self.promien = promien

    def pole(self):
        return math.pi * self.promien ** 2
    
class Trojkat(Ksztalt):
    def __init__(self, nazwa, a, b, c):
        super().__init__(nazwa)
        self.a = a
        self.b = b
        self.c = c

    def pole(self):
        p = (self.a + self.b + self.c)/ 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Prostokat(Ksztalt):
    def __init__(self, nazwa, a, b):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b
    

class Kwadrat(Prostokat):
    def __init__(self, bok):
        super().__init__("Kwadrat", bok, bok)

class TrojkatRownoboczny(Trojkat):
    def __init__(self, bok):
        super().__init__("Trójkąt równoboczny", bok, bok, bok)


def main():
    figury = [
        Kolo("Koło", 5),
        Trojkat("Trójkąt", 3, 4, 5),
        Prostokat("Prostokąt", 2, 6),
        Kwadrat(4),
        TrojkatRownoboczny(3)
    ]

    for figura in figury:
        print(f"{figura.nazwa}: pole = {figura.pole():.2f}")


if __name__ == "__main__":
    main()

    
