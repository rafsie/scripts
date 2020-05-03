# Zad. 5.3 (1 pkt)
# N = 100 osob (osoba = watek) rozwaza pojscie do kina na konkretny seans. Watki te
# startuja jednoczesnie i kazdy watek po losowej liczbie sekund (od 1 do 4s, tylko
# calkowita liczba sekund) namyslu podejmuje decyzje z prawdopodobienstwem
# "pozytywnym" (tj. wyjscia do kina) p1 = 0,05. Kino nie wyswietla filmu, jesli nie
# zbierze sie minimum 5 widzow. W takim przypadku trzeba wyswietlic napis typu:
# "Przepraszamy, filmu nie bedzie." i program sie konczy.
# W przeciwnym wypadku wyswietla sie film, którego symulowany czas trwa 4s. Ale
# film jest nudny i dokladnie w polowie seansu kazdy z widzow podejmuje decyzje: wyjsc
# (z prawdopodobienstwem p2 = 0,3) lub zostac. Jesli liczba osob, które została nadal
# wynosi >= 5, to film jest kontynuowany. Jesli nie, to film zostaje przerwany, a
# kierownictwo kina wypisuje obrazliwy komunikat (o frajerach i o tym, ze pieniedzy za
# bilety nie oddaja...).

import threading
import random
import sys


class Osoba(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print('Osob:', self.h)
        x = random.randint(1, 4)
        event = threading.Event()
        event.wait(x)
        if (random.random() < 0.05) == True:
            thread = Widz('')
            thread.start()
        return  # Close threads


class Widz(threading.Thread):
    _counter = 0

    def __init__(self, j):
        threading.Thread.__init__(self)
        self.h = j
        Widz._counter += 1
        self.id = Widz._counter

    def run(self):
        pass


if __name__ == '__main__':

    for i in range(1, 101):
        thread = Osoba(i)
        thread.start()

    event = threading.Event()
    event.wait(5)  # Wait for threads termination
    print('\nWidzow:', Widz._counter)

    if (Widz._counter) < 5:
        print('Przepraszamy, filmu nie bedzie.')
        sys.exit()

    else:
        print('Zapraszamy na film...')
        event.wait(2)
        viewcounter = 0
        for viewer in range(Widz._counter):
            if (random.random() < 0.3) == True:
                viewcounter += 1
        print('Pozostalo: {} widzow'.format(viewcounter))
        if viewcounter >= 5:
            print('...ciąg dalszy filmu')
            event.wait(2)
        else:
            print('Koniec ogladania, nie zwracamy za bilety!')
