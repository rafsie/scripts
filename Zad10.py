# Zad. 4.1 (1 pkt)
# W pliku dane.txt (do ściągnięcia lokalnie) są dane osobowe: imię nazwisko kraj zarobki.
# Należy wypisać sumę zarobków 2 najlepiej i 2 najgorzej zarabiających Polaków (PL) – prawidłowy wynik: 101999 i 38900.
# Ponadto dla każdego kraju występującego w pliku należy wypisać liczbę osób, w kolejności pojawiania się krajów 
# w kolejnych wierszach. Czyli: PL - 6, DE - 2, CZ - 3, US - 2.

class Person(object):
    def __init__(self, name, surname, country, salary):
        self.name = name
        self.surname = surname
        self.country = country
        self.salary = salary

    def __repr__(self):
        return repr((self.name, self.surname, self.country, self.salary))

    @staticmethod
    def reader():
        with open('dane.txt', 'r') as file:
            mainlst = []
            for line in file:
                sublst = []
                for word in line.split():
                    if word.isalpha():
                        sublst.append(word)
                    else:
                        sublst.append(int(word))
                mainlst.append(Person(sublst[0], sublst[1], sublst[2], sublst[3]))
        return mainlst


if __name__ == '__main__':

    persons = Person.reader()
    persons_sorted = (sorted(persons, key=lambda person: person.salary))
    salaries = list(obj.salary for obj in persons_sorted if obj.country == 'PL')

    print(salaries[4] + salaries[5])
    print(salaries[0] + salaries[1])

    print('\nPL -', sum(obj.country.count('PL') for obj in persons))
    print('DE -', sum(obj.country.count('DE') for obj in persons))
    print('CZ -', sum(obj.country.count('CZ') for obj in persons))
    print('US -', sum(obj.country.count('US') for obj in persons))
