#1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.
def bmi_value(mass_person,growth):
    bmi = mass_person / (growth ** 2)
    return bmi


def bmi_opinion(bmi):
    if bmi < 18.5 and bmi >= 16:
        return print('Masz niedowagę.')
    elif bmi >= 25 and bmi < 30:
        return print('Masz nadwagę.')
    elif bmi >= 18.5 and bmi < 25:
        return print('BMI w normie.')
    elif bmi >= 30:
        return print('To już otyłość..')
    else:
        return print('Nie żyjesz albo masz same kości :P')


mass_person = int(input('Jaka jest Twoja waga [kg]'))
growth = float(input('Jaki jest Twój wzrost [m]'))

bmi_opinion(bmi_value(mass_person, growth))

#2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość
# z 3 liczb. minimum_of(a, b, c).


def min_nb_in_list(a, b, c):
    if a < b < c:
        print(f"Najmniejszą liczbą jest {a}")
    elif b < a < c:
        print(f"Najmniejszą liczbą jest {b}")
    else:
        print(f"Najmniejszą liczbą jest {c}")


min_nb_in_list(3, 6, 10)

#3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość ]
# z 3 liczb. maximum_of(a, b, c).


def max_nb_in_list(a, b, c):
    if a > b >c:
        print(f"Największą liczbą jest {a}")
    elif b > a > c:
        print(f"Największą liczbą jest {b}")
    else:
        print(f"Największą liczbą jest {c}")


max_nb_in_list(3, 6, 10)

#4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić
# komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.


def check_nb(min, max, nb):
    if nb > min and nb < max:
        print(f'Liczba {nb} ZNAJDUJE się w zakresie liczb od {min} do {max}.')
    else:
        print(f'Liczba {nb} NIE ZNAJDUJE się w zakresie liczb od {min} do {max}.')


min_input = int(input("Podaj najniższą wartość zakresu: "))
max_input = int(input("Podaj najwyższą wartość zakresu: "))
nb_input = int(input("Podaj liczbę do sprawdzenia: "))

check_nb(min_input, max_input, nb_input)

#5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.


def cold_warm(nb_of_user, sweet_spot):
    range_to_ss = nb_of_user - sweet_spot
    if range_to_ss > 0 and range_to_ss <= 10:
        print('Gorąco!!!')
    elif range_to_ss > 0 and 20 >= range_to_ss > 10:
        print('Ciepło...')
    elif range_to_ss < 0 and range_to_ss >= -10:
        print('Gorąco!!!')
    elif range_to_ss < 0 and -20 <= range_to_ss < -10:
        print('Ciepło...')
    elif range_to_ss > 20 or range_to_ss < -20:
        print('Zimno......')
    else:
        print(f'Trafiłeś! Uryta liczba to {sweet_spot} !')
        return exit()

hidden_nb = int(50)

for i in range(1, 11):
    shoot = int(input(f"Próba nr.{i}! Podaj liczbę: "))
    cold_warm(shoot, hidden_nb)

print(f"Niestety nie trafiłeś.. Ukrytą liczbą była liczba: {hidden_nb}")

#6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
# -------------- Znajduje się w pliku K-N-P_game -----------------

