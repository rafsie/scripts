# Zad. 5.2 (1,5 pkt)
# Napisz aplikacje wielowatkowa wypisujaca na konsoli napisy z tablicy po znaku,
# z zachowaniem kolejnosci watkow w kazdej „rundzie”. Dokładniej: na poczatku 
# kazdy watek wypisuje po jednym znaku – to jest pierwsza runda. W nastepnych 
# rundach watki wypisuja tez po znaku, w kolejnosci watkow okreslonych przez 
# pierwsza runde. Gdy dany watek zakonczy swoja prace (tj. skoncza mu sie znaki), 
# wtedy oczywiscie jest pomijany.

import threading


class Mythread(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i
        self.lst = ['aaaa', 'bb', 'ccccccccccccc', 'dddddd']
        self._key_lock = threading.Lock()

    def run(self):
        self._key_lock.acquire()  # Critical section
        for i in range(len(max(self.lst, key=len))):
            x = list(map(''.join, [s[i:i + 1] for s in self.lst]))
            y = "".join(x)
            print(y, end=' ')
        self._key_lock.release()  # Critical section


if __name__ == '__main__':
    thread1 = Mythread(1)
    thread1.start()
    thread2 = Mythread(2)
    thread2.start()
    thread3 = Mythread(3)
    thread3.start()
    thread4 = Mythread(4)
    thread4.start()
