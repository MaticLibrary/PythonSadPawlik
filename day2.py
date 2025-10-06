
# print("Podaj Imie:")
# first_name = input()
# print("Imie:", first_name)
# print("Podaj Nazwisko:")
# last_name = input()
# print(first_name, "ma na Nazwisko:" , last_name)

x = input('Podaj wartosc dla x: ')
y = input('Podaj wartosc dla y: ')

print("Dodawanie:", x, '+', y , '=', int(x) + int(y))
print("Odejmowanie:", x, '-', y ,'=', int(x) - int(y))
print("Mnozenie: ", x ,'*', y , '=', int(x) * int(y) )
print("Dzielenie: ", x, '/', y, '=', float(x) / float(y))
print("Dzielenie calkowite: ", x, '//', y, '=', int(x) // int(y))
print("Modulo: ", x, '%', y, '=', int(x) % int(y))
print("Potegowanie: ", x, '**', y, '=', int(x) ** int(y))

if(x.isdigit() and y.isdigit()):
    if(int(x) == int(y)):
        print(x, 'jest rowne', y)
    if(int(x) != int(y)):
        print(x, 'nie jest rowne', y)
    if(int(x) > int(y)):
        print(x, 'jest wieksze od', y)
    if(int(x) < int(y)):
        print(x, 'jest mniejsze od', y)
else:
    print('Nie okreslony blad')


staticListtuple = tuple(range(100, -1, -2))

print("Lista statyczna tuple liczb parzystych od 100 do 0: pętlą for")
for i in staticListtuple:
    print(i)

print("Samo print:", staticListtuple)
#   staticListtuple[2] = int(staticListtuple[2] + 1)  nie da się zmienić elementu tuple
#   print("Samo print po zmianie 3 elementu tuple:", staticListtuple)

dynaminList = list(range(100, -1, -3))
print("Lista dynamiczna range liczb co 3 od 100 do 0: pętlą for")

for i in dynaminList:
    print(i)

print("Samo print:", dynaminList)

# da sie zmieniac wartosci w liscie
dynaminList[2] = dynaminList[2] + 1
dynaminList.sort(reverse=True)
print("Samo print po zmianie 3 elementu listy:", dynaminList)

# wordbook ??? some matrix
wordbook = {
    'username': 'admin',
    'passoword': 'admin1234',
    'age': 30,
    'isMarried': False,
    'hobbies': ['sport', 'programming', 'reading'],
    'pets': {
        'dog': 'Burek',
        'cat': 'Mruczek'
    }
}
