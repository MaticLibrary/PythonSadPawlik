import sys

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_decorator
def liczba_na_slowa(napis):
    liczby = {
        '0': 'zero', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery',
        '5': 'pięć', '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć'
    }
    slowny_napis = ""
    for i, znak in enumerate(napis, 1):
        if znak in liczby:
            slowny_napis += liczby[znak] + " "
        else:
            slowny_napis += f"Znak nr {i} nie jest liczbą "
    return slowny_napis.strip()


@uppercase_decorator
def drukuj(*args, sep=" ", end="\n"):
    wynik = sep.join(map(str, args))
    return wynik + end


if __name__ == "__main__":
    print(liczba_na_slowa("1410"))
    print(drukuj(192, 168, 0, 1, sep=":"))
    print(drukuj("Temperatura wynosi", 36.6, "stopni"))
