import math
from abc import ABC, abstractmethod

# --- KLASY FIGUR PŁASKICH --- #

class Ksztalt(ABC):
    def __init__(self, nazwa: str):
        self.__nazwa = nazwa

    @property
    def nazwa(self):
        return self.__nazwa

    @abstractmethod
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
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Prostokat(Ksztalt):
    def __init__(self, nazwa, a, b):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b


# --- FIGURY FOREMNE --- #

class Kwadrat(Prostokat):
    def __init__(self, bok):
        super().__init__("Kwadrat", bok, bok)
        self.liczba_bokow = 4


class TrojkatRownoboczny(Trojkat):
    def __init__(self, bok):
        super().__init__("Trójkąt równoboczny", bok, bok, bok)
        self.liczba_bokow = 3


# --- BRYŁY --- #

class Bryla(Ksztalt):
    def __init__(self, nazwa, sciany):
        super().__init__(nazwa)
        self.sciany = sciany  # lista obiektów figur

    def pole(self):
        # suma pól wszystkich ścian
        return sum([sciana.pole() for sciana in self.sciany])


# --- Mixin: dla brył platońskich (czworościan, sześcian) --- #

class Platon:
    def wierzcholki(self):
        liczba_scian = len(self.sciany)
        liczba_bokow_sciany = self.sciany[0].liczba_bokow
        return int(2 - liczba_scian + liczba_scian * liczba_bokow_sciany / 2)


# --- KONKRETNE BRYŁY --- #

class Czworoscian(Bryla, Platon):
    def __init__(self, bok):
        sciany = [TrojkatRownoboczny(bok) for _ in range(4)]
        super().__init__("Czworościan", sciany)


class Szescian(Bryla, Platon):
    def __init__(self, bok):
        sciany = [Kwadrat(bok) for _ in range(6)]
        super().__init__("Sześcian", sciany)


class Piramida(Bryla):
    def __init__(self, bok):
        sciany = [TrojkatRownoboczny(bok) for _ in range(4)] + [Kwadrat(bok)]
        super().__init__("Piramida", sciany)

    def wierzcholki(self):
        return 5


# --- MAIN --- #

def main():
    bryly = [
        Czworoscian(3),
        Szescian(2),
        Piramida(4)
    ]

    for bryla in bryly:
        pole = bryla.pole()
        if hasattr(bryla, "wierzcholki"):
            w = bryla.wierzcholki()
        else:
            w = "brak danych"
        print(f"{bryla.nazwa}: pole = {pole:.2f}, liczba wierzchołków = {w}")


if __name__ == "__main__":
    main()
