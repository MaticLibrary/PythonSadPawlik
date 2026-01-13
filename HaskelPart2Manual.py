add(N)           # Dodaj N
mul(N)           # Pomnóż przez N
flip(pow)(N)     # Podnieś do potęgi N
flip(truediv)(N) # Podziel przez N
flip(gt)(N)      # Większe niż N (x > N)
flip(lt)(N)      # Mniejsze niż N (x < N)
eq(N)            # Równe N
f ** g           # Złożenie (g potem f)
map(f)           # Zastosuj f do każdego
filter(w)        # Filtruj według warunku w
sum              # Suma elementów

# Stwórz funkcję  add_1, która będzie zwiększać każdy element podanej jej listy o 1.
# Funkcja ma być stworzona poprzez uzupełnienie zapisu:
# add_1 =   
# bez lambdy z wykorzystaniem częściowej aplikacji funkcji add i map
# Za pomocą tej funkcji powiększ o jeden wszystkie elementy listy  [1,2,3,4,5,6].
# Stwórz funkcję  less_3, która będzie usuwać podanej jej listy elementy większe lub równe 3.
# Funkcja ma być stworzona poprzez uzupełnienie zapisu:
# less_3 =   
# bez lambdy z wykorzystaniem częściowej aplikacji funkcji fliter, gt lub lt i flip
# Za pomocą tej funkcji usuń z listy [1,2,3,4,3,2,1] wszystkie elementy >=3

from haskell import flip, add, lt, map, filter

add_1 = map(add(1))
less_3 = filter(flip(lt)(3)) 

def main():
    lista1 = [1, 2, 3, 4, 5, 6]
    wynik1 = list(add_1(lista1))
    print(f"add_1({lista1}) = {wynik1}")
    
    lista2 = [1, 2, 3, 4, 3, 2, 1]
    wynik2 = list(less_3(lista2))
    print(f"less_3({lista2}) = {wynik2}")

if __name__ == "__main__":
    main()




#  Cezar  

from haskell import flip, add, map, mod
from haskell import Haskell

@Haskell
def nakod(c):
    return ord(c)

@Haskell
def naznaki(k):
    return chr(k)

def Cezar(napis, klucz):
    return map(naznaki ** (flip(mod)(127)) ** add(klucz) ** nakod)(napis)

# Przykład użycia:
if __name__ == "__main__":
    tekst = "Hello"
    klucz = 3
    zaszyfrowany = Cezar(tekst, klucz)
    print(''.join(zaszyfrowany))  # Powinno wypisać: Khoor


#####################

# Chcemy: funkcja dzieląca przez 2
dziel_przez_2 = lambda x: x / 2

# ŹLE:
truediv(2)  # lambda x: 2 / x (odwrotność!)

# DOBRZE:
flip(truediv)(2)  # lambda x: x / 2

##########################
# CHCEMY: funkcja f(x) = x OPERACJA N
# ZAMIENIAMY: flip(operacja)(N)

# Dzielenie przez N:
flip(truediv)(N)  # x / N

# Mniejsze niż N:
flip(lt)(N)  # x < N

# Większe niż N:
flip(gt)(N)  # x > N

# Modulo N:
flip(mod)(N)  # x % N

# Potęga N:
flip(pow)(N)  # x ** N

