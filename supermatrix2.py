# Tabliczka mnożenia
# Użytkownik podaje liczbę
# Program wyświetla wyniki mnożenia tej liczby od 1 do 10
# Rozszerzenie: zrób całą tabliczkę 1–10 (w pętli zagnieżdżonej)


def matrix(wartosc):
    print("   ", end="")
    for j in range(wartosc + 1):
        print(f"{j:4}", end="")  
    print("\n" + "-" * (5 * (wartosc + 1)))

    for i in range(wartosc + 1):
        print(f"{i:2} |", end="")  
        for j in range(wartosc + 1):
            print(f"{i*j:4}", end="")
        print()  


def main():
    liczba = int(input("Podaj wartosc: "))
    matrix(liczba)


if __name__ == "__main__":
    main()


