def bmi_judge(bmi):
    if bmi < 18.5 and bmi >= 1:
        verdict = 'niedowaga'
    elif bmi > 25 and bmi < 30:
        verdict = 'nadwaga'
    elif bmi > 18.5 and bmi < 25:
        verdict = 'waga normalna'
    elif bmi >= 30:
        verdict = 'otyłość'
    else:
        verdict = 'Nie żyjesz albo masz same kości :P \n' \
                  'Za niskie BMI by mogło być prawdziwe!!!'
    return verdict


def bmi_value(weight, growth):
    bmi = int(weight / (growth ** 2))
    return bmi
