import time

zakres = eval(input("Podaj zakres poszukiwania liczby doskonałej:"))

lista1 = []
lista2 = []

start_time = time.time()

for i in range(1, zakres+1):
    for j in range(1, i+1):
        if (i % j == 0):
            lista1.append(j)
    suma = sum(lista1)
    lista1.clear()
    if (suma-i == i):
        lista2.append(i)
print("Liczby doskonałe:", lista2)

end_time = time.time()

elapsed_time = end_time-start_time
print("Czas wyszukiwania:", elapsed_time, "s")
