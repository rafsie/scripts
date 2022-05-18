# Zad. 1.1 (1 pkt)
# W kodzie programu mamy zmienną: int liczba = 0b1101_1000;
# Napisz program konwertujący tę liczbę na system 10-tny, 3-kowy lub 16-kowy (w zależności od wyboru użytkownika).
# Program ma wczytywać podstawę w postaci tekstowej: „dziesięć”, „trzy” lub „szesnaście”
# (jeśli użytkownik wpisze coś innego, to ma być wypisany stosowny komunikat).


def ternary(n):
    quot = n / 3
    remain = n % 3
    if quot == 0:
        return ""
    else:
        return ternary(int(quot)) + str(int(remain))


liczba = 0b1101_1000
strnum = bin(liczba)

base = input("Podaj podstawę - dziesiec, trzy lub szesnascie:")

if base == 'dziesiec':
    result = int(strnum, 2)
    print(result)
elif base == 'trzy':
    result = ternary(liczba)
    print(result)
elif base == 'szesnascie':
    result = hex(liczba)
    print(result)
else:
    print("Niepoprwana podstawa!")
    
