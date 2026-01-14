from haskell import add, mod, flip, Haskell

#   G o t o w e 

@Haskell
def nakod(c):
    return ord(c)

@Haskell  
def naznaki(k):
    return chr(k)

def szyfrCezaraPetla(napis, key):
    napisPoSzyfr = ""
    for litera in napis:
        napisPoSzyfr += chr(mod(add(ord(litera))(key))(127))
    return napisPoSzyfr

def szyfrCezara(napis, key):
    return ''.join(map(naznaki ** (flip(mod)(127)) ** add(key) ** nakod, napis))

def main():
    tekst = "Ala ma kota"
    klucz = 3
    print(szyfrCezaraPetla(tekst,klucz))
    print(szyfrCezara(tekst, klucz))
    print(szyfrCezara(szyfrCezara(tekst, klucz), -klucz))

if __name__ == "__main__":
    main()




#####################################################################################
from haskell import pow, flip, truediv, sum, map

sq = flip(pow)(2)
sqrt = flip(pow)(0.5)

def dlugoscWektora(wektor):
    return sqrt(sum(map(sq, wektor)))

dlugoscWektora2 = sqrt ** sum ** map(sq)

def normalizacjaWektora(wektor):
    return map(flip(truediv)(dlugoscWektora(wektor)), wektor)

def main():
    wektor = [1, 2, 3, 4, 5]
    
    print("Pierwsza wersja:", dlugoscWektora(wektor))
    print("Druga wersja:   ", dlugoscWektora2(wektor))
    
    print("\nZnormalizowany wektor:")
    znormalizowany = list(normalizacjaWektora(wektor))
    print(znormalizowany)
    
    print("Pierwsza wersja:", dlugoscWektora(znormalizowany))
    print("Druga wersja:   ", dlugoscWektora2(znormalizowany))

if __name__ == "__main__":
    main()

#######################################################################

from functools import partial
import operator

def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

def flip(f):
    def flipped(x, y):
        return f(y, x)
    return flipped

def szyfrCezara_czysty(napis, key):
    nakod = ord
    naznaki = chr
    add_key = partial(operator.add, key)
    mod127 = partial(flip(operator.mod), 127)
    koduj_znak = compose(naznaki, compose(mod127, compose(add_key, nakod)))
    return ''.join(map(koduj_znak, napis))

sq = partial(flip(operator.pow), 2)
sqrt = partial(flip(operator.pow), 0.5)

def dlugoscWektora_czysty(wektor):
    return sqrt(sum(map(sq, wektor)))

map_sq = partial(map, sq)
dlugoscWektora2_czysty = compose(sqrt, compose(sum, map_sq))

def normalizacjaWektora_czysty(wektor):
    d = dlugoscWektora_czysty(wektor)
    return map(partial(flip(operator.truediv), d), wektor)

def main():
    tekst = "Ala ma kota"
    klucz = 3
    
    zaszyfrowany = szyfrCezara_czysty(tekst, klucz)
    print(zaszyfrowany)
    
    odszyfrowany = szyfrCezara_czysty(zaszyfrowany, -klucz)
    print(odszyfrowany)
    
    wektor = [1, 2, 3, 4, 5]
    print(dlugoscWektora_czysty(wektor))
    print(dlugoscWektora2_czysty(wektor))
    
    znormalizowany = list(normalizacjaWektora_czysty(wektor))
    print(znormalizowany)
    
    print(dlugoscWektora_czysty(znormalizowany))
    print(dlugoscWektora2_czysty(znormalizowany))

if __name__ == "__main__":
    main()
