ilosc = eval(input("Podaj ilość liczb ciągu Fibonacciego:"))
a = 0
b = 1
for i in range(1, ilosc + 1):
    c = a + b
    print(b, end=' ')
    a = b
    b = c
