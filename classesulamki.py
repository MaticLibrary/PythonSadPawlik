# Napisz klasę reprezentującą ułamki zwykłe niewłaściwe. Obiekt tej klasy ma być tworzony
# poprzez podanie licznika i mianownika. Klasa ma obsługiwać operacje: dodawanie, odejmowanie,
# mnożenie i dzielenie ułamków zwykłych. Operacje powinny wykorzystywać standardowe
# operatory tych działań (+, -, *, /) (podpowiedź: zdefiniuj dla tej klasy odpowiednie metody
# specjalne). Po operacjach ułamki powinny zostać skrócone.
# Do realizacji np. dodawania przyda się metoda licząca najmniejszą wspólną wielokrotność
# (NWW). NWW można wyliczyć obliczając wcześniej największy wspólny dzielnik dwóch liczb
# (NWD). Ta metoda również przyda się przy skracaniu ułamków. Obie metody zaimplementuj jako
# prywatne.
# Zdefiniuj także odpowiednią metodę specjalną, aby można wypisywać ułamek zwykły w postaci
# licznik/mianownik. Np. ułamek u o liczniku 3 i mianowniku 4 powinien w wyniku
# wywołania print(u) wyświetlić:
# 3/4

class Ulamek:
    def __init__(self, licznik, mianownik):                       # konstruktor
        if mianownik == 0:                                        #       
            raise ValueError("Mianownik nie moze byc rowny Zero") #
        self.licznik = licznik                                    #
        self.mianownik = mianownik                                #
        
        self.__skroc()   # automatyczne skrocenie z metody prywatnej klasy

    def __nwd(self, a, b): # najwiekszy wspolny dzielnik
        while(b != 0):
            a, b = b, a % b
        return abs(a)
    def __nww(self, a, b):  # najmniejsza wspolna wielokrotnosc
        return abs(a * b) // self.__nwd(a, b)
    def __skroc(self):      # __nazwa  to sie daje dla prywatnej metody 
        nwd = self.__nwd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd

    def __add__(self, other):
        print("self:", self.licznik, "/", self.mianownik)
        print("other:", other.licznik, "/", other.mianownik)
        print ("Wynik tego dodawania to: ")
        nww = self.__nww(self.mianownik, other.mianownik)
        nowy_licznik = (self.licznik * (nww // self.mianownik)) + (other.licznik * (nww // other.mianownik))
        return Ulamek(nowy_licznik, nww)

    def __sub__(self, other):
        print("self:", self.licznik, "/", self.mianownik)
        print("other:", other.licznik, "/", other.mianownik)
        print ("Wynik tego odejmowania to: ")
        nww = self.__nww(self.mianownik, other.mianownik)
        nowy_licznik = (self.licznik * (nww // self.mianownik)) - (other.licznik * (nww // other.mianownik))
        return Ulamek(nowy_licznik, nww)

    def __mul__(self, other):
        print("self:", self.licznik, "/", self.mianownik)
        print("other:", other.licznik, "/", other.mianownik)
        print ("Wynik tego mnozenia to: ")
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__(self, other):
        print("self:", self.licznik, "/", self.mianownik)
        print("other:", other.licznik, "/", other.mianownik)
        print ("Wynik tego dzielenia to: ")
        return Ulamek(self.licznik * other.mianownik, self.mianownik * other.licznik)

    # --- Reprezentacja tekstowa ---
    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"



def main():
    u1 = Ulamek(1, 2)   # 1/2
    u2 = Ulamek(3, 4)   # 3/4
    u3 = Ulamek(10, 20) # 1/2 po skróceniu

    print("Ułamek 1:", u1)
    print("Ułamek 2:", u2)
    print("Ułamek 3:", u3)

    print("\n--- Działania ---")
    print(f"{u1} + {u2} = {u1 + u2}")
    print(f"{u1} - {u2} = {u1 - u2}")
    print(f"{u1} * {u2} = {u1 * u2}")
    print(f"{u1} / {u2} = {u1 / u2}")

if __name__ == "__main__":
    main()
    
