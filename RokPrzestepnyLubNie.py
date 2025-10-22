def czy_przestepny(rok):
    if(rok % 4 == 0):
        if(rok % 100 == 0):
            if(rok % 400 == 0):
               return print("Rok jest przestepny - sklada sie z 366 dni. ")
    else:
        return print("Rok normlany. ")

def main():
    rok = int(input("Podaj rok do sprawdzenia: "))
    czy_przestepny(rok)

if __name__ == "__main__":
    main()
