import random

moje_punkty = 0
komp_punkty = 0

for i in range(5):
    wyb = input("\nPapier, kamień, nożyce? (p/k/n):")

    if wyb == 'p' or wyb == 'P':
        moj_wyb = 'Papier'
    elif wyb == 'k' or wyb == 'K':
        moj_wyb = 'Kamień'
    elif wyb == 'n' or wyb == 'N':
        moj_wyb = 'Nożyce'
    else:
        print("Zły wybór!")
        continue

    print("Ty:", moj_wyb)

    lista = ['Papier', 'Kamień', 'Nożyce']
    wyb_komp = random.choice(lista)
    print("Komputer:", wyb_komp)

    if moj_wyb == 'Papier' and wyb_komp == 'Papier':
        print("Remis!")
    elif moj_wyb == 'Papier' and wyb_komp == 'Kamień':
        print("Wygrałeś!")
        moje_punkty += 1
    elif moj_wyb == 'Papier' and wyb_komp == 'Nożyce':
        print("Wygrywa Komputer!")
        komp_punkty += 1
    elif moj_wyb == 'Kamień' and wyb_komp == 'Papier':
        print("Wygrywa Komputer!")
        komp_punkty += 1
    elif moj_wyb == 'Kamień' and wyb_komp == 'Kamień':
        print("Remis!")
    elif moj_wyb == 'Kamień' and wyb_komp == 'Nożyce':
        print("Wygrałeś!")
        moje_punkty += 1
    elif moj_wyb == 'Nożyce' and wyb_komp == 'Papier':
        print("Wygrałeś!")
        moje_punkty += 1
    elif moj_wyb == 'Nożyce' and wyb_komp == 'Kamień':
        print("Wygrywa Komputer!")
        komp_punkty += 1
    elif moj_wyb == 'Nożyce' and wyb_komp == 'Nożyce':
        print("Remis!")

if moje_punkty > komp_punkty:
    print("\nWygrałeś starcie:", moje_punkty, "do", komp_punkty)
elif moje_punkty < komp_punkty:
    print("\nStarcie wygrywa Komputer:", moje_punkty, "do", komp_punkty)
elif moje_punkty == komp_punkty:
    print("\nRemis w starciu:", moje_punkty, "do", komp_punkty)
