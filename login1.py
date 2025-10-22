def logowanie(expected_login, expected_password):
    print("Witaj użytkowniku!\n\nLogowanie:\n")
    login_test = input("Wprowadź nazwę użytkownika: ").strip()
    if login_test != expected_login:
        print("Nie znaleziono takiego użytkownika!")
        return False

    temp = 4
    while temp > 0:
        haslo = input("Podaj hasło: ").strip()
        if haslo == expected_password:
            print("Pomyślnie zalogowano!")
            return True
        temp -= 1
        if temp > 0:
            print(f"Hasło niepoprawne. Pozostało prób: {temp}. Spróbuj ponownie.")
        else:
            print("Konto zablokowane.")  
            return False       


def main():
    login = "admin"
    password = "admin1234"
    logowanie(login,password)




if __name__ == "__main__":
    main()
