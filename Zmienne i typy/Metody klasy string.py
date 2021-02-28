# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch
# złożony z trzech środkowych znaków danego ciągu.
word = 'hipopotam'
print(word[int((len(word)//2)-1):int((len(word)//2)+2)])
print('*'*100)

# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1 = 'góra'
s2 = 'dół'

half = int(len(s1)//2)

print(s1[0:half]+s2+s1[half:])
print('*'*100)

# 3. "Do zmiennej quote przypisz zdanie(...)"
quote = 'Honesty is the first chapter in the book of wisdom.'

print(len(quote))

print(quote[-7: -1: 1])

print(quote[-1])

mid = len(quote)//2
print(quote[mid::3])

print(quote[::2])

print(quote[::-1])

print(quote.replace('wisdom', 'friendship'))
print('*'*100)

# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie(...)
title = input('Podaj tytuł książki: ',)
scname = input('Podaj nazwisko autora książki:',)
nrpages = input('Podaj liczbę stron: ',)
print(title.isalpha())
print(scname.isalpha())
print(nrpages.isdigit())
print('Tytuł ksiązki to "', title.capitalize(), '"',)
print('Autor ksiązki ma na nazwisko ', scname.capitalize())
book = str(title+' ' + scname+' ' + nrpages)
print(book)
print(len(book))
print('*'*100)

# 5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy
# wprowadzone wyrażenie jest palindromem.
word = input('Podaj wyrażenie: ')
wordreverse = word[::-1]
print("Czy jest to palidrom: ", word == wordreverse)
print('*'*100)

# 6. Nie dałem rady tego zrobić..

# 7.
speed = 300000
what = str('światła')
print("Prędkość {} wynosi ok. {} km/s.".format(what,speed))