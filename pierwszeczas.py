import time

numFrom = eval(input("Podaj liczbe poczatkowa: "))
numTo = eval(input("Podaj liczbe koncowa: "))

start_time = time.time()

lista = []
for i in range(numFrom, numTo):
    for x in range(2,i):
        if (i % x) == 0:
            break
        else:
            if(x == i - 1):
                 lista.append(i)
    if(i == numTo - 1):
            print("Liczby pierwsze: {}".format(lista))

end_time = time.time()
elapsed_time = end_time-start_time
print("\nCzas:", elapsed_time, "s")
