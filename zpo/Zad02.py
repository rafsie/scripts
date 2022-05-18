# Zad. 1.2 (1 pkt)
# Napisz funkcję, która analizuje numer PESEL i wyciąga datę urodzenia oraz płeć danej osoby.
# Te dane są zwracane jako obiekt odpowiedniej (utworzonej) klasy.
# Przekazany do funkcji argument może być niepoprawny jako PESEL, też obsłuż taką sytuację
# (albo przez rzucenie stosownego wyjątku albo w inny sposób).

from datetime import datetime, date


def controlnum(pesel):
    numpesel = list(int(i) for i in pesel)
    bases = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3]
    sum = 0

    for i in range(0, len(numpesel)):
        sum += numpesel[i] * bases[i]

    return sum % 10


def datesex(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    sex = ''

    if 0 < month < 13:
        year += 1900
    elif 20 < month < 33:
        year += 2000
        month -= 20
    elif 40 < month < 53:
        year += 2100
        month -= 40
    elif 60 < month < 73:
        year += 2200
        month -= 60
    elif 80 < month < 93:
        year += 1800
        month -= 80

    if int(pesel[9]) % 2 == 1:
        sex = 'M'
    else:
        sex = 'K'

    return year, month, day, sex


strPesel = input("Podaj numer PESEL: ")

if strPesel.isnumeric() is False or len(strPesel) != 11 or controlnum(strPesel) != 0:
    print("Niepoprawny numer PESEL!")
    exit()
else:
    strdate = str(datesex(strPesel))[1:-6]
    dt = datetime.strptime(strdate, "%Y, %m, %d")

    if dt > datetime.today():
        print("Niepoprawny numer PESEL!")
        exit()
    else:
        print('Data urodzenia: {}-{}-{}'
              '\nPlec: {}'.format(datesex(strPesel)[0],
                                  datesex(strPesel)[1],
                                  datesex(strPesel)[2],
                                  datesex(strPesel)[3]))
