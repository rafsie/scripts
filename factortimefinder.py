import time

number = eval(input("Podaj liczbę całkowitą:"))
factor = []

start_time = time.time()

for i in range(1, number // 2 + 1):
    if (number % i == 0):
        factor.append(i)

end_time = time.time()
print(factor)

elapsed_time = end_time-start_time
print("\nCzas:", elapsed_time, "s")
