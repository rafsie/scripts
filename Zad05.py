# Zad. 2.2
# Napisz klase zawierajaca metody sortujace napisy z uwzglednieniem 
# alfabetu polskiego (np. „Łukasz” ma byc miedzy „Lucyna” a „Marek”).

import time
import locale

# Sortowanie 1
start_time1 = time.time()

for i in range(100000):
    names1 = ["Łukasz", "Ścibor", "Stefania", "Darek", "Agnieszka", "Zyta", "Órszula", "Świetopełk"]
    names1.sort()
print("Sortowanie 1:", names1)

end_time1 = time.time()


# Sortowanie 2
class User:
    def __init__(self, name):
        self.name = name


Lukasz = User('Łukasz')
Scibor = User('Ścibor')
Stefania = User('Stefania')
Darek = User('Darek')
Agnieszka = User('Agnieszka')
Zyta = User('Zyta')
Orszula = User('Órszula')
Swietopelk = User('Świetopełk')

start_time2 = time.time()

for i in range(100000):
    L = [Lukasz, Scibor, Stefania, Darek, Agnieszka, Zyta, Orszula, Swietopelk]
    L.sort(key=lambda x: x.name)
print("Sortowanie 2:",[item.name for item in L])

end_time2 = time.time()


# Sortowanie 3
start_time3 = time.time()

for i in range(100000):
    names3 = ["Łukasz", "Ścibor", "Stefania", "Darek", "Agnieszka", "Zyta", "Órszula", "Świetopełk"]
    locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")
    names3.sort(key=locale.strxfrm)
print("Sortowanie 3:", names3)

end_time3 = time.time()


elapsed_time1 = end_time1-start_time1
print("\nCzas sortowania 1:", elapsed_time1, "sek.")

elapsed_time2 = end_time2-start_time2
print("Czas sortowania 2:", elapsed_time2, "sek.")

elapsed_time3 = end_time3-start_time3
print("Czas sortowania 3:", elapsed_time3, "sek.")

