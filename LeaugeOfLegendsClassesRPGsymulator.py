from abc import ABC, abstractmethod
from random import randint

class Postac:
    def __init__(self, imie, poziom, punkty_zycia=20):
        self.imie = imie
        self.poziom = poziom
        self.punkty_zycia = punkty_zycia
        print(f"Tworzenie postaci: {self.imie} (Poziom {self.poziom})")

    def atak(self, przeciwnik):
        obrazenia = randint(1, 5)
        przeciwnik.punkty_zycia -= obrazenia
        print(f"{self.imie} atakuje {przeciwnik.imie} i zadaje {obrazenia} obrażeń!")

    def opis(self):
        print(f"{self.imie} (Poziom: {self.poziom}, HP: {self.punkty_zycia})")

    def mozliwoscUniku(self):
        if hasattr(self, "unik") and randint(1, 10) <= self.unik:
            print(f"{self.imie} unika ataku!")
            return True
        return False

    @staticmethod
    def porownaj_poziomy(postac1, postac2):
        if postac1.poziom > postac2.poziom:
            print(f"{postac1.imie} jest silniejszy poziomem niż {postac2.imie}")
        elif postac1.poziom < postac2.poziom:
            print(f"{postac2.imie} jest silniejszy poziomem niż {postac1.imie}")
        else:
            print("Obie postacie mają ten sam poziom!")

    @classmethod
    def z_danych(cls, tekst):
        imie, poziom, hp = tekst.split(",")
        return cls(imie.strip(), int(poziom), int(hp))


class Assassin(Postac):
    def __init__(self, imie, poziom, punkty_zycia=18, unik=7, sila=6):
        super().__init__(imie, poziom, punkty_zycia)
        self.unik = unik
        self.sila = sila
        print(f"Tworzenie Assassina: {self.imie}")

    def atak(self, przeciwnik):
        if przeciwnik.mozliwoscUniku():
            print(f"{przeciwnik.imie} uniknął ataku!")
            return
        obrazenia = randint(5, 10) + self.sila
        przeciwnik.punkty_zycia -= obrazenia
        print(f"{self.imie} atakuje {przeciwnik.imie} i zadaje {obrazenia} obrażeń!")


class Wojownik(Postac):
    def __init__(self, imie, poziom, punkty_zycia=25, sila=8, unik=2):
        super().__init__(imie, poziom, punkty_zycia)
        self.sila = sila
        self.unik = unik
        print(f"Tworzenie Wojownika: {self.imie}")

    def atak(self, przeciwnik):
        if przeciwnik.mozliwoscUniku():
            print(f"{przeciwnik.imie} uniknął ataku!")
            return
        obrazenia = randint(3, 8) + self.sila
        przeciwnik.punkty_zycia -= obrazenia
        print(f"{self.imie} uderza {przeciwnik.imie} i zadaje {obrazenia} obrażeń!")


def menu():
    print("\n--- MENU ---")
    print("1. Opis postaci")
    print("2. Atak")
    print("3. Porównaj poziomy")
    print("4. Stwórz nową postać z tekstu")
    print("5. Wyjście")
    return input("Wybierz opcję: ")


def main():
    wojownik = Wojownik("Xin Zhao", 12)
    assassin = Assassin("Zed", 15)

    while True:
        wybor = menu()

        if wybor == "1":
            wojownik.opis()
            assassin.opis()

        elif wybor == "2":
            print("\nKto atakuje?")
            print("1. Wojownik")
            print("2. Assassin")
            wybor_atak = input("> ")

            if wybor_atak == "1":
                wojownik.atak(assassin)
            elif wybor_atak == "2":
                assassin.atak(wojownik)
            else:
                print("Niepoprawny wybór.")

        elif wybor == "3":
            Postac.porownaj_poziomy(wojownik, assassin)

        elif wybor == "4":
            dane = input("Podaj dane w formacie 'Imie,Poziom,HP': ")
            nowa_postac = Postac.z_danych(dane)
            nowa_postac.opis()

        elif wybor == "5":
            print("Zakończono program.")
            break

        else:
            print("Nie ma takiej opcji.")


if __name__ == "__main__":
    main()
