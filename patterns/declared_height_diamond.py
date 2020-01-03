x = eval(input("Podaj wysokość:"))
wys = int(x/2)+(x%2)
for i in range(wys):
    print(' '*(wys-i), '*'*(i+(i+1)))
if(x%2 == 0):
    for i in range(wys, 0, -1):
        print(' '*(wys-(i-1)), '*'*(i+(i-1)))
else:
    for i in range(wys-1, 0, -1):
        print(' '*(wys-(i-1)), '*'*(i+(i-1)))
