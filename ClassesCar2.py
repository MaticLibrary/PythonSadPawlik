class Samochod:
    def __init__(self, marka, model, predkosc = 0):
        self.marka = marka
        self.model = model
        self.predkosc = predkosc

    def drukuj(self):
        print (f"Samochod: {self.marka} {self.model}")

    def przyspieszenie(self):
        self.predkosc +=  15
        return self.predkosc
    
    def zwolnij(self):
        self.predkosc = max(0, self.predkosc - 10)
        return self.predkosc
    
    def pokaz_predkosc(self):
        return print(f"predkoc samochodu: {self.predkosc}")
    
    @classmethod
    def from_string(cls, car_string):
        marka, model = car_string.split(' ')
        return cls(marka, model)


def main():
    print("Welcome..,\n")
    modelTooClass = input("Podaj wartosc dla modelu: ")
    markaTooClass = input("Podaj wartosc dla marki: ")
    car1 = Samochod(markaTooClass,modelTooClass)
    car1.drukuj()
    car1.przyspieszenie()
    car1.przyspieszenie()
    car1.przyspieszenie()
    car1.zwolnij()
    car1.pokaz_predkosc()


if __name__ == "__main__":
    main()
