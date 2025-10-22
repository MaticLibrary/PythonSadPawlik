
def czy_parzysta(liczba):
    if(liczba % 2 == 0):
        return print("Parzysta ")
    else:
        print("liczba nieparzysta... ")

def main():
    liczba = int(input("Podaj liczbe do sprawdzenia: "))
    czy_parzysta(liczba)
if __name__ == "__main__": 
    main()
    
