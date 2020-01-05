n = int(input("Podaj wysokość w wierszach:"))
polowa = int(n/2)+1
for wiersz in range(1,n+1):
    for kolumna in range(1,n*2):
        if (wiersz+kolumna==n+1 or kolumna-wiersz==n-1):
            print("*",end="")
        elif (wiersz==polowa and kolumna>n-polowa and kolumna<n+polowa):
            print("*",end="")
        else:
            print(" ",end="")
    print()
