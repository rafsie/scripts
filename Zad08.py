# Zad. 3.2 (1,5 pkt)
# Podstawową modelu ma być interfejs Publikacja, w którym są deklaracje metod zwracających autora, 
# tytuł i liczbę stron publikacji. Publikację implementuje klasa konkretna Ksiazka (zawierająca 
# odpowiednie pola, czyli posiadająca stan). Dla książki k przedefiniuj m.in. funkcję toString(…), 
# tak aby instrukcja: System.out.println(k); wyświetlała tekst w rodzaju:
# | Adam Mickiewicz | Pan Tadeusz | 340 |
# Przyklad uzycia dekoratorow w Pythonie:

def decorator(argument):
    def book_decorator(func):
        def func_wrapper(name):
            return "{1} {0} |".format(argument, func(name))
        return func_wrapper
    return book_decorator


class Ksiazka(object):
    def __init__(self, autor, tytul, liczbastron):
        self.autor = autor
        self.tytul = tytul
        self.liczbastron = liczbastron
        self.opis = '| ' + self.autor + ' | ' + self.tytul + ' | ' + self.liczbastron + ' |'


    @decorator('KsiazkaZObwoluta')
    @decorator('KsiazkaZOkladkaZwykla')
    def method_a(self):
        return self.opis

    @decorator('KsiazkaZObwoluta')
    @decorator('KsiazkaZOkladkaTwarda')
    def method_b(self):
        return self.opis

    @decorator('Drogiej Hani - Adam Mickiewicz')
    @decorator('KsiazkaZOkladkaZwykla')
    def method_c(self):
        return self.opis


k1 = Ksiazka('Adam Mickiewicz', 'Pan Tadeusz', '340')
k2 = Ksiazka('Adam Mickiewicz', 'Dziady', '130')

print(k1.method_a())
print(k1.method_b())
print(k1.method_c())
print()
print(k2.method_a())
print(k2.method_b())
print(k2.method_c())
