x = eval(input("Podaj wysokość:"))
for i in range(x):
    print(' '*(x-i), '*'*(i+(i+1)))
