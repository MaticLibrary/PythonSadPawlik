
import random

def zgaduj_zgadula():
    liczba_do_zgadniecia = random.randint(1,10)
    liczba = 11
    szanse = 3

    print(liczba_do_zgadniecia)

    print("Zgaduj liczba z przedzialu 1- 10")

    while (liczba_do_zgadniecia != liczba and szanse > 0):
        
        liczba = int(input("Wprowadz swoja wartosc do zgadywania: "))
        if(liczba_do_zgadniecia > liczba):
            szanse = szanse - 1
            print("Twoja liczba jest mniejsza od wylosowanej. \n")
        if(liczba_do_zgadniecia < liczba):
            szanse = szanse - 1
            print("Twoja liczba jest wieksza od zgadywanej. \n")
        if(szanse == 0):
            print("Nie udalo sie zgadnac w okrelonych probach. ")
            return 0
        if(liczba_do_zgadniecia == liczba):
            print("\n\nGratulacje udalo ci sie zgadnac. ")
            return 0


def main():
    print("Witaj w zgaduj zgadula!")
    zgaduj_zgadula()


if __name__ == "__main__": 
    main()
    
