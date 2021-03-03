# 1. Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
names = input('Wpisz kilka imion rozdielonych przecinkiem:')
names = names.replace(' ','').split(',')

for n in names:
    print('Hello',n.title(),'!')

# 2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
text = input('Podaj jakiś tekst: ')
print(text[::2])

x = len(text)
for i in range(1,x,2):
    print("{}".format(text[i]),end= '')

# 3. W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
textin = input('Podaj ciąg znaków: ')
x = 0
y = 0
z = 0
f = 0

for small in textin:
    if small.islower():
        x=x+1
    if small.isdigit():
        y=y+1
    if small.isupper():
        z=z+1
    if not small.isalnum():
        f=f+1

print('Małych liter jest:',x,'Dużych liter jest:',z,'Cyfr jest:',y,'Znaków specjalnych i stacji:',f)

# 4.  Napisz grę - kamień (k) / papier (p) / nożyce (n).
import random
rund = int(input("Podaj liczbę rund: "))
shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
seq = ('k','p','n')
AI = random.choice(seq)

for runda in range(1, rund, 1):
   if shoot == AI:
    print('Remis w',runda,'rundzie!')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
   elif shoot == 'k' and AI == 'p':
    print('Komputer wygrał',runda,'rundę..')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
   elif shoot == 'k' and AI == 'n':
    print('Wygrałeś ',runda,'rundę!')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
   elif shoot == 'p' and AI == 'n':
    print('Komputer wygrał',runda,'rundę..')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
   elif shoot == 'p' and AI == 'k':
    print('Wygrałeś ',runda,'rundę!')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
   elif shoot == 'n' and AI == 'k':
    print('Komputer wygrał',runda,'rundę..')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
   elif shoot == 'n' and AI == 'p':
    print('Wygrałeś ',runda,'rundę!')
    AI = random.choice(seq)
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")

