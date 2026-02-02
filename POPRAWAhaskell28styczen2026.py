# 11 : 30    G r u p a  I  30 minut czasu

# Zadanie 1 odejmij_7 Haskell, wywołanie przez upe print(odejmij_7, [4,3,25])

# Zadanie 2 Usun z listy wszystkie slowa zaczynajace sie od podanej litery, nie wolno uzywac def, jedynie lambda,

# Zadanie 3 Suma krotek rekurencja ogonowa, [(5,4),(3,3),(2,1),(2,4),(7,5)]  => [9, 6, 3, 6, 12]

# Zadanie 4 Normalizacja Wektora


# 13:00 Grupa II

# Zadanie I  Stworz funckje do_trzeciej, ktora kazdy element otrzymanej listy podniesie do 3 potegi.
#            Nalezy zastosowac czesciowa aplikacje,  Nie wolno uzyc slow def ani lambda

# Zadanie II Napisz rekurencyjna, funckje sr_war liczaca srednia i wariancje wedulg wzorow.  Funckja ma zwracac krotke zawierajaca srednia i wariancje listy.  Niech srednia bedzie
#            liczona jak w rekurencji ogonowej (w trakcie schodzenia w głąb), a wariancja przy powrotach w 'górę'. Funckja powinna mieć 3 parametry: listę, długość listy oraz sumę
#            (do wyliczenia średniej, ustawiona na początku na wartość domyślną 0)
#
#            UWAGA - parametr długosc ma przechowywac poczatkowa dlugosc listy(te z main-a) a nie dlugosc pierszego elementu z kolejnych wywolan
#            Liczenie sredniej moze byc identyczne jak ogonowe liczenie sumy elementow listy, a kiedy lista bedzie pusta, nalezy zamiast zwrocenia sumy, zwrocic krotke: sume podzielna
#            przez długość oraz 0 początkujące zliczanie sumy kwadratów.
#            Natomiast zliczanie wariancji przebiega jak liczenie sumy w rekurencji zwyklej tyle, ze sumujemy kwadraty roznic dzielone przez dlugosc i zwracamy krotke (Srednia, dotychczasowa wariancja)
#            UWAGA: ZAKAZ funckji    sum

# Zadanie III Napisz funckje dłuższe_od, która otrzyma liste list (wektorów) i zostawi na niej te wektory, których długość przekracza podaną, jako drugi argument, wartóść. 
#             Długość wektora rozumiemy jako: pierwiastek sumy kwadratów jego elementów - to powinno być liczone w funkcji pomocniczej stworzonej przez skłądnie funckji
#             realiujacych wymienione operacje (czyli użycie ** a nie def)
#
#             Funckja dłuższe_od może być utworzona za pomocą def, inne użycie def nie jest dozwolone (trzeba wykorzystac skłądnie funckji operatorem **),
#             Nalezy wykorzystac funckje filter. Nie jest dozwolone uzycie wyrazenia lambda
#             Do dyspozycji sąfunckje odpowiadające operatorom <, <=, >= i > czyli lt, le, ge, gt oraz funckje pow, sum, map, flip.

#  PODPOWIEDZ PAWLIKA:  funckje filter powinna otrzymac zlozenie czesciowo zaaplikowanej ktorejs z funckji <, <=, >=, i >  z funckji liczącą długosc wektora.

# Zadanie IV Napisz funckje o nazwie iloczyn_parrzystych, ktora liczy iloczyn elementów listy o parzystych wartosciach. Funckja ma wykorzystac funckje reduce oraz lambda
#            NIE uzywamy tu modułu haskell, NIE WOLNO uzyc slowa def

#  Grupa III  15:00
#  Zadanie I Napisz funckje o nazwie euklides, ktora liczy odleglosc euklidesowa pomiedzy dwoma punktami (reprezentowanymi jako listy lub krotki) Np. (1,2) to punkt na plaszczyznie a [1,4,5] punkt w
#            przestrzeni trojwymiarowej. Funckja ma wykorzstac funckje reduce i zip (oraz oczywiscie sqrt). Mozna wykorzstac map, sub, pow (ale nie jest to konieczne). Funckje reduce i map nie są
#            importowane z modulu Haskell (a wiec nie mozna ich skladac operatorem ** ani czesciowo aplikowac)
#            Dla przypomnienia odleglsoc punktow to pierwiastek sumy kwadratow roznic wspolrzednych - np odleglosc miedzy [1,3] i [4,7] wyniesie 5 (czyli euklides([1,3], [4,7]) ma zwrocic 5)

#  Zadanie II. Napisz funckje indeksy, ktora w sekwencji znajdzie indesky wystapien podanego elementu. Funckja ma otrzymywac sekwencje i element a zwracac liste indeksow znalezionych wystapien
#              uzywamy snd, fst, filter, map

#  Zadanie III. Stworz funckje przez_3, ktora kazdy element otrzymanej listy podzieli przez 3. Nalezy wykorzystac czeciowa aplikacje, nie wolno uzywac def, lambda ani mul

#  Zadanie IV   Policz iloczyn listy elementowej, iloczyn parzystych, w liscie sa liczby le to nie trzeba udowadniac, lista pusta ma iloczyn 1, rekurencja ogonowa, uzyc match


#  IV grupa    16 : 45
#              Zadanie I:  mod z flipem reszta_3  =  flip(mod)(3)
#              Zadanie II: dodac do siebie po przez rekurencje (nie ogonowa)  dla [(1,2), (3,4)] => [3,7]
#              Zadanie III: usunac samogloski z wyrazow  map, reduce
#              Zadanie IV:  Najwiekszy element z listy poprzez reduce, trzeba obliczyc maksimum za pomoca samego reduce


