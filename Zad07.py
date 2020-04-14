import sys
import json
import random
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt5.QtCore import pyqtSlot


class Reader:
    def __init__(self):
        self.readjson()

    def readjson(self):
        with open('PolEngTest.json', encoding='utf-8') as r:
            data = json.load(r)
        return data


class Writer:
    def __init__(self):
        super().__init__()

    def writejson(self, data):
        with open('imie_nazwisko.json','w') as w:
            json.dump(data, w, ensure_ascii=False)
        return data


class AddToDict(dict):
    def __init__(self):
        super().__init__()
        self.dict = dict()

    def add(self, key, value):
        self[key] = value


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Test znajomości słówek'
        self.left = 800
        self.top = 400
        self.width = 320
        self.height = 140
        self.initUI()
        self.counter = 0
        self.questansw = AddToDict()

    def draw(self):
        r = Reader()
        self.words = (random.sample((r.readjson().keys()), 5))
        print(self.words)
        return self.words

    def initUI(self):
        global start_time
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label1 = QLabel("Podaj angielskie tłumaczenie słówka:", self)
        label1.move(20, 10)
        label1.adjustSize()
        self.label2 = QLabel('tekst do zamiany', self)
        self.label2.move(20, 30)
        self.label2.adjustSize()

        # create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 60)
        self.textbox.resize(280, 20)

        # create a button in the window
        self.button = QPushButton('OK', self)
        self.button.move(110, 95)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

        # set label / start time
        self.draw()
        self.label2.setText(self.words[0])
        start_time = time.time()

    def time_printer(self):
        elapsed_time = end_time - start_time
        print("Czas: {:0.2f} sek.".format(elapsed_time))
        return round(elapsed_time, 2)

    @pyqtSlot()
    def on_click(self):
        global end_time
        if self.counter < 5:
            textboxvalue = self.textbox.text()
            self.questansw.add(self.label2.text(), textboxvalue.lower())
            self.textbox.setText("")
            print(self.questansw)

            try:
                self.label2.setText(self.words[self.counter+1])

            except IndexError:

                end_time = time.time()
                self.close()
                l = Levenshtein()
                r = Reader()
                x = r.readjson()
                score = 0

                for i in range(len(self.words)):
                    #print("\nWpisane:", self.questansw[self.words[i]]) # what I type (for test purposes)
                    #print("Możliwe prawidłowe:", x[(self.words)[i]]) # all possible correct answers (for test purposes)

                    (x[self.words[i]]) = (x[self.words[i]]) if isinstance((x[self.words[i]]), list) else [(x[self.words[i]])]
                    values = []
                    for item in (x[self.words[i]]):
                        values.append(l.levscore(item, (self.questansw[self.words[i]])))

                    values.sort()

                    if values[0] == 0:
                        score += 1
                    elif values[0] == 1:
                        score += 0.5
                    else:
                        score += 0

                print()
                total_time = self.time_printer()
                print("Punkty:", score)
                self.questansw.add("czas", total_time)
                self.questansw.add("punkty", score)
                print("Zawartość zapisanego pliku:", self.questansw)
                w = Writer()
                w.writejson(self.questansw)
                QMessageBox.information(self, 'Wyniki', "Czas: {:0.2f} sek.<br /> Punkty: {}< br />".format(total_time, score), QMessageBox.Ok, QMessageBox.Ok)

            self.counter += 1

        else:
            sys.exit(app.exec_())


class Levenshtein():
    def __init__(self):
        super().__init__()

    def levscore(self, s1, s2):
        d = {}
        lenstr1 = len(s1)
        lenstr2 = len(s2)
        for i in range(-1, lenstr1 + 1):
            d[(i, -1)] = i + 1
        for j in range(-1, lenstr2 + 1):
            d[(-1, j)] = j + 1

        for i in range(lenstr1):
            for j in range(lenstr2):
                if s1[i] == s2[j]:
                    cost = 0
                else:
                    cost = 1

                d[(i, j)] = min(
                    d[(i - 1, j)] + 1,
                    d[(i, j - 1)] + 1,
                    d[(i - 1, j - 1)] + cost,
                )

                if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                    d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)

        return d[lenstr1 - 1, lenstr2 - 1]


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
