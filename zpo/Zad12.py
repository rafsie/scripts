# Zad. 4.3 (1,5 pkt)
# Jan uczy się słówek angielskich. Każdego dnia przyswaja 2 nowe słowa.
# Niestety, każdego dnia również zapomina co najwyżej 2 słowa spośród tych, których nauczył się >= 3 dni wcześniej.
# Każdego dnia losujemy 2 słowa spośród słów poznanych >= 3 dni wcześniej (jeśli w ogóle takie istnieją)
# i zapominamy każde z nich z prawdopodobieństwem p = 0,5. Jan może się nauczyć słów, które już wcześniej zapomniał.

import random
import numpy as np

class Learning:
    def __init__(self):
        self.learn()

    def learn(self):
        with open('1500.txt', 'r') as f:
            words = f.read().splitlines()

        new, forgotten, known = [], [], []

        for n in range(0,10):
            print("\nDay:", n+1)
            new = random.sample(words, 2)
            print("New words:", new)
            for item in new:
                words.remove(item)
            known.extend(new)

            if n >= 3:
                toforget = np.sum(np.random.choice(2, 2, replace=True, p=[0.5, 0.5]))
                forgotten = random.sample(known[:-4], toforget)
                print("Forgotten words:", forgotten)
                for item in forgotten:
                    known.remove(item)
                words.extend(forgotten)
            print("Known:", known)

        print("\nAll known:", known)


if __name__ == '__main__':
    l = Learning()
    l.learn()
