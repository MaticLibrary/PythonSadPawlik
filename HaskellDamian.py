import inspect
from operator import add, sub
from functools import reduce


class Haskell:
    def __init__(self, func, num_args = None):
        signature = inspect.signature(func)
        self.num_args = len(signature.parameters)
        self.func = func

    def __pow__(self, other):
        return lambda *args, **kw: self.func(other(*args, **kw))

    def __call__(self, *a):
        if len(a) == self.num_args:
            return self.func(*a)

        def q(*b):
            return self.func(*(a + b))

        return Haskell(q, self.num_args - len(a))


def flip(f):
    return Haskell(lambda y, x: f(x, y))


# odejmij 7
flip_sub = flip(sub)
odemij_7 = map(flip_sub(7), [13, 8, 15, 12, 14])


# suma listy krotek rekurencyjnie
def sum_tuples_rec(lst, result=None):
    if result is None:
        result = []

    match lst:
        case []:
            return result
        case [(a, b), *rest]:
            current_sum = a + b
            result.append(current_sum)
            return sum_tuples_rec(rest, result)


# lista napisów (przykładowe filtrowanie)
filtered_words = list(filter(lambda word: word[0] != letter, words))


# dodaj 7
flip_add = Haskell(add, 2)
dodaj_7 = map(flip_add(7), [13, 8, 15, 12, 14])


# dodaj parzyste rekurencyjnie
def sumowanie_rekurencyjne_parzyste(lista, wynik=0):
    match lista:
        case []:
            return wynik
        case [glowa, *reszta]:
            if glowa % 2 == 0:
                wynik = glowa + wynik
            return sumowanie_rekurencyjne_parzyste(reszta, wynik)


def sumowanie(lista, wynik = 0):
    match lista:
        case[]:
            return wynik
        case[glowa, *reszta]:
            if glowa % 2 == 0:
                wynik += glowa
    return sumowanie(reszta, wynik)
