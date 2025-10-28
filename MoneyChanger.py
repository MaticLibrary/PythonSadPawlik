# Zamiana walut na PLN
# Data: 28 października 17:17

def ChangerOfValue(kwota):
    mapOfValue = {'USD': 4.2, 'EUR': 4.5, 'GBP': 5.2}
    waluta = input("Wprowadź walutę (USD, EUR, GBP): ").upper()

    # Sprawdzenie, czy waluta istnieje w słowniku
    if waluta in mapOfValue:
        przelicznik = mapOfValue[waluta]
        wynik = kwota * przelicznik
        print(f"1 {waluta} = {przelicznik} PLN")
        return round(wynik, 2)
    else:
        print("Brak takiej waluty. Spróbuj ponownie.")
        return None


def main():
    try:
        saldo = float(input("Wprowadź kwotę do przeliczenia: "))
    except ValueError:
        print("Podano błędną wartość! Wpisz liczbę.")
        return

    displayValue = ChangerOfValue(saldo)
    if displayValue is not None:
        print(f"Twoja kwota w PLN to: {displayValue} zł")

if __name__ == '__main__':
    main()
