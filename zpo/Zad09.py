# Zad. 3.3 (1 pkt)
# Korzystając z Date and Time API Javy 8 (opisane skrótowo w Java_2020_03.ppt, S76+) policz: a, b, c, d.

import datetime


class Days:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count(self):
        date_format = "%d-%m-%Y"
        a = datetime.datetime.strptime(self.x, date_format)
        b = datetime.datetime.strptime(self.y, date_format)
        return b - a


d = Days('01-09-1939', '08-05-1945')
print(d.count())


class Date:
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def calculatedate(self):
        date = datetime.date(self.year, 1, 1)
        diff = datetime.timedelta(self.day - 1)
        newdate = date + diff
        return newdate


c = Date(2016, 68)
print(c.calculatedate())


class SumFifteen:
    def __init__(self, starthour, endhour, csum):
        self.starthour = starthour
        self.endhour = endhour
        self.csum = csum

    def calcsum(self):
        start = datetime.datetime.strptime(self.starthour, '%H:%M')
        end = datetime.datetime.strptime(self.endhour, '%H:%M')

        dtlst=[]
        hourlst=[]
        counter = 0

        while start <= end:
            dtlst.append(start)
            start += datetime.timedelta(minutes=1)

        for d in dtlst:
            hourlst.append(d.strftime("%H%M"))

        for n in hourlst:
            x = 0
            for element in n:
                x += int(element)
                if x == self.csum:
                    counter += 1
                    print(n[:2]+':'+n[2:], end=' | ')

        print("\nLiczba godzin o sumie cyfr {}: {}".format(self.csum, counter))

s = SumFifteen('11:45', '22:30', 15)
s.calcsum()


class Leapyear:
    def __init__(self, year):
        self.year = year

    def februaries(self):
        x = 0
        currentYear = datetime.datetime.now().year
        if self.year < currentYear:
            for i in range(self.year, currentYear):
                if ((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):
                    x = x + 1
            print("Przeżyłeś {} razy 29 lutego od roku {}.".format(x, self.year))
        else:
            print("Niepoprawny rok!")
        return x

l = Leapyear(1995)
l.februaries()
