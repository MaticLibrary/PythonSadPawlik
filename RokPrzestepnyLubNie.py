def czy_przestepny(rok):
    if rok % 400 == 0:
        return True
    elif rok % 100 == 0:
        return False
    elif rok % 4 == 0:
        return True
    else:
        return False

def main():
    rok = int(input("Podaj rok do sprawdzenia: "))
    if czy_przestepny(rok):
        print("Rok jest przestępny - składa się z 366 dni.")
    else:
        print("Rok jest zwykły - składa się z 365 dni.")

if __name__ == "__main__":
    main()
