def matrix(wartosc):
    for i in range(11):
        print(i, " * ", wartosc,"= ", wartosc*i )

def main():
    liczba = int(input("Podaj liczbe dla tabliczki mnoezenia: "))
    matrix(liczba)

if __name__ == "__main__":
    main()
