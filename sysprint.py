import sys

def drukuj(*args, sep=" ", end="\n"):
    wynik = ""
    for arg in args:
        wynik += str(arg) + sep
    wynik = wynik[:-len(sep)]
    sys.stdout.write(wynik + end)


if __name__ == "__main__":
    drukuj(192, 168, 0, 1, sep=":")
    temperatura = 36.6
    drukuj("Temperatura wynosi", temperatura, "stopni")
    for _ in range(10):
        drukuj("*", end="")
