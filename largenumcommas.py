s1 = input("Podaj dużą liczbę całkowitą:")
s2 = ","
s3 = ""
counter = 1
for i in range(len(s1), 0, -1):
    if counter % 3 == 0 and i > 1:
        s3 += s1[i-1] + s2
    else:
        s3 += s1[i-1]
    counter += 1
s3 = s3[::-1]
print(s3)
