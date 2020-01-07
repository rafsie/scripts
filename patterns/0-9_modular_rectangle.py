szer = eval(input("Podaj szerokość:"))
wys = eval(input("Podaj wysokość:"))
if szer<0 or wys<0:
    print("Niepoprawne dane!")
    exit()
temp1, temp2 = 0, 0
while temp2 != wys:
    for i in range(10):
        print(i, end=' ')
        temp1 += 1
        if temp1 == szer:
            temp1 = 0
            print()
            temp2 += 1
        if temp2 == wys:
            break
