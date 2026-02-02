# 11 : 30    G r u p a  I  30 minut czasu

# Zadanie 1 odejmij_7 Haskell, wywołanie przez upe print(odejmij_7, [4,3,25])
HaskellSub = Haskell(sub, 2)
Sub_7 = flip(sub)(7)
odejmij_7 = list(map(Sub_7, lista))

# Zadanie 2 Usun z listy wszystkie slowa zaczynajace sie od podanej litery, nie wolno uzywac def, jedynie lambda,
# usuwanie_litery = lambda lista_slow, litera: list(filter(lambda slowo: slowo[0] != litera, lista_slow))
usuwanie_literki = lambda lista_slow, litera: filter(lambda slowo: slowo[0] != litera, lista_slow)


# Zadanie 3 Suma krotek rekurencja ogonowa, [(5,4),(3,3),(2,1),(2,4),(7,5)]  => [9, 6, 3, 6, 12]

def suma_krotek_ogon(lista, wynik = []):
    if not lista:
        return wynik
    glowa, *reszta = lista
    return suma_krotek_ogon(reszta, wynik[glowa[0] + glowa[1]]) 
        

# Zadanie 4 Normalizacja Wektora, podzielenie kazdego elementu poprzez dlugosc - pierwiastek sumy kwadratow     .   Mamy uzyc lifta
#   bez def, moze byc lambda
#                           [4,2,3]
dlugosc = flip(pow)(0.5) ** sum ** map(flip(pow)(2))
normalizacja_wektora = lambda wektor: map(flip(truediv)(dlugosc(wektor)), wektor) 

# lift
dlugosc = lift1(flip(pow)(0.5)) ** reduce(lift2(lambda acc, x: acc + x)) ** map(lift1(flip(pow)(2)))
normalizacja_wektora = lambda wektor: map(flip(lift2(truediv))(dlugosc(wektor)), wektor)


# 13:00 Grupa II

# Zadanie I  Stworz funckje do_trzeciej, ktora kazdy element otrzymanej listy podniesie do 3 potegi.
#            Nalezy zastosowac czesciowa aplikacje,  Nie wolno uzyc slow def ani lambda
HaskPow = Haskel(pow, 2)
Pow3 = flip(pow)(3)
do_trzeciej = list(map(Pow3, lista))


# Zadanie II Napisz rekurencyjna, funckje sr_war liczaca srednia i wariancje wedulg wzorow.  Funckja ma zwracac krotke zawierajaca srednia i wariancje listy.  Niech srednia bedzie
#            liczona jak w rekurencji ogonowej (w trakcie schodzenia w głąb), a wariancja przy powrotach w 'górę'. Funckja powinna mieć 3 parametry: listę, długość listy oraz sumę
#            (do wyliczenia średniej, ustawiona na początku na wartość domyślną 0)
#            UWAGA - parametr długosc ma przechowywac poczatkowa dlugosc listy(te z main-a) a nie dlugosc pierszego elementu z kolejnych wywolan
#            Liczenie sredniej moze byc identyczne jak ogonowe liczenie sumy elementow listy, a kiedy lista bedzie pusta, nalezy zamiast zwrocenia sumy, zwrocic krotke: sume podzielna
#            przez długość oraz 0 początkujące zliczanie sumy kwadratów.
#            Natomiast zliczanie wariancji przebiega jak liczenie sumy w rekurencji zwyklej tyle, ze sumujemy kwadraty roznic dzielone przez dlugosc i zwracamy krotke (Srednia, dotychczasowa wariancja)
        #    UWAGA: ZAKAZ funckji    sum
def sr_war(lista, dlugosc, suma=0):
    if not lista:  
        srednia = suma / dlugosc if dlugosc > 0 else 0
        return (srednia, 0)  
    sr, war = sr_war(lista[1:], dlugosc, suma + lista[0])
    war += (lista[0] - sr) ** 2 / dlugosc
    
    return (sr, war)

#   DOBRE
def sr_war(lista, dlugosc, suma = 0):
    if not lista:       #[srednia, wariancja]
        return suma/dlugosc, 0
    glowa, *reszta = lista
    srednia, wariancja = sr_war(reszta, dlugosc, suma + glowa)
    return srednia, wariancja + (glowa - srednia)**2/(dlugosc -1)

# Zadanie III Napisz funckje dłuższe_od, która otrzyma liste list (wektorów) i zostawi na niej te wektory, których długość przekracza podaną, jako drugi argument, wartóść. 
#             Długość wektora rozumiemy jako: pierwiastek sumy kwadratów jego elementów - to powinno być liczone w funkcji pomocniczej stworzonej przez skłądnie funckji
#             realiujacych wymienione operacje (czyli użycie ** a nie def)
#
#             Funckja dłuższe_od może być utworzona za pomocą def, inne użycie def nie jest dozwolone (trzeba wykorzystac skłądnie funckji operatorem **),
#             Nalezy wykorzystac funckje filter. Nie jest dozwolone uzycie wyrazenia lambda
#             Do dyspozycji są funckje odpowiadające operatorom <, <=, >= i > czyli lt, le, ge, gt oraz funckje pow, sum, map, flip.
#  PODPOWIEDZ PAWLIKA:  funckje filter powinna otrzymac zlozenie czesciowo zaaplikowanej ktorejs z funckji <, <=, >=, i >  z funckji liczącą długosc wektora. 

def dluzsze_od(lista_wektorow, wartosc):
    dlugosc_wektora = flip(pow)(0.5) ** sum ** map(flip(pow)(2)) 
    return filter(le(wartosc) ** dlugosc_wektora, lista_wektorow)

# Zadanie IV Napisz funckje o nazwie iloczyn_parrzystych, ktora liczy iloczyn elementów listy o parzystych wartosciach. Funckja ma wykorzystac funckje reduce oraz lambda
#            NIE uzywamy tu modułu haskell, NIE WOLNO uzyc slowa def
iloczyn_parzystych = lambda lista: reduce(lambda acc, x: acc * x if x % 2 == 0 else acc, lista, 1)

#  Grupa III  15:00
#  Zadanie I Napisz funckje o nazwie euklides, ktora liczy odleglosc euklidesowa pomiedzy dwoma punktami (reprezentowanymi jako listy lub krotki) Np. (1,2) to punkt na plaszczyznie a [1,4,5] punkt w
#            przestrzeni trojwymiarowej. Funckja ma wykorzstac funckje reduce i zip (oraz oczywiscie sqrt). 
# Mozna wykorzstac map, sub, pow (ale nie jest to konieczne). Funckje reduce i map nie są
#            importowane z modulu Haskell (a wiec nie mozna ich skladac operatorem ** ani czesciowo aplikowac)
#            Dla przypomnienia odleglosc punktow to pierwiastek sumy kwadratow roznic wspolrzednych - np odleglosc miedzy 
# [1,3] i [4,7] wyniesie 5 (czyli euklides([1,3], [4,7]) ma zwrocic 5)
def euklides(p1, p2):
#    return sqrt(reduce(lambda acc, x: acc + pow(sub(x[0], x[1]),2), zip(p1, p2), 0))
    return sqrt(reduce(lambda acc, x: acc + (x[0] - x[1]) ** 2, zip(p1, p2)))

#  Zadanie II. Napisz funckje indeksy, ktora w sekwencji znajdzie indesky wystapien podanego elementu. Funckja ma otrzymywac sekwencje i element i zwracac liste indeksow znalezionych wystapien
#              uzywamy snd, fst, filter, map
#       fst indeks      snd liczba
def indeksy(sekwnecja, element):
    return map( fst, filter(eq(element) ** snd, enumerate(sekwnecja)))

#  Zadanie III. Stworz funckje przez_3, ktora kazdy element otrzymanej listy podzieli przez 3. Nalezy wykorzystac czeciowa aplikacje, nie wolno uzywac def, lambda ani mul
haskdziel = Haskell(sub, 2)
hask = flip(haskdziel)(3)
przez_3 = map(hask, lista)

#  Zadanie IV   Policz iloczyn listy elementowej, iloczyn parzystych, w liscie sa liczby ale to nie trzeba udowadniac, lista pusta ma iloczyn 1, rekurencja ogonowa, uzyc match
def iloczyn_ogonowy(lista, wynik = 1):
    match lista:
        case[]:
            return wynik
        case[glowa, *reszta]:
            if glowa % 2 == 0:
                wynik *= 1
            return iloczyn_ogonowy(reszta, wynik)



#  IV grupa    16 : 45
#              Zadanie I:  mod z flipem reszta_3  =  flip(mod)(3)
HaskFlip  = Haskel(mod, 2)
reszta_3flip = flip(HaskFlip)(3)
reszta_3 = map(reszta_3flip, lista) 
#              Zadanie II: dodac do siebie po przez rekurencje (nie ogonowa)  dla [(1,2), (3,4)] => [3,7]
def dodwanie_krotek(lista_krotek):
    if not lista_krotek:
        return []
    glowa, *reszta = lista_krotek
    return [glowa[0] + glowa[1]] + dodwanie_krotek(reszta)

#              Zadanie III: usunac samogloski z wyrazow  map, reduce
usuwanie_samoglosek = lambda lista_slow: reduce(map(lambda slowo: filter(lambda litera: litera not in "ioueya"),slowo) , lista_slow)

#
usun_samo = lambda lista_slow: map(lambda napis: reduce(lambda acc, litera: acc + ''.join(litera) if litera not in "aeiouy" else acc , napis, '') , lista_slow)

#              Zadanie IV:  Najwiekszy element z listy poprzez reduce, trzeba obliczyc maksimum za pomoca samego reduce

najwiekszy_element = lambda lista: reduce(lambda acc,  x:  x if x > acc else acc, lista )




#   DODATKOWE


#       szyfr Cezara
def Cezar(slowo, key):
    return ''.join(map litera: ord ** mod()())
