# Zad. 5.1 (0,5 pkt)
# Napisz program tworzacy 10 watków, kazdy tylko wypisujacy: Hello from task x, gdzie x
# bedzie jego numerem (0..9), ale jako pierwszy ma wypisac swój komunikat watek ostatni
# (tj. nr 9), potem przedostatni, itd. do pierwszego.

import threading
import time


class Mythread(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print('Hello from task:', self.h)


if __name__ == '__main__':

    for i in range(9, -1, -1):
        thread = Mythread(i)
        thread.start()
        time.sleep(0.3)
