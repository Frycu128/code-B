print("Moje BMI wynosi około", 62//(1.8*1.8))

# BMI = (masa (kg)) / (wzrost (m))²
waga = 62
wzrost = 1.8
BMI = waga / (wzrost ** 2)
BMI_rounded = round(BMI, 2)
print('Moje BMI =', BMI_rounded)

waga = int(input('Jaka jest Twoja waga [kg]'))
wzrost = float(input('Jaki jest Twój wzrost [m]'))

BMI = int(waga/(wzrost**2))
print('Moje BMI=', BMI)
