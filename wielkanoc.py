import math

year = eval(input("Podaj rok:"))
cen = math.floor(year / 100)
m = (15 + cen - (math.floor(cen / 4)) - (math.floor((8 * cen + 13) / 25))) % 30
n = (4 + cen - (math.floor(cen / 4))) % 7
a = year % 4
b = year % 7
c = year % 19
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7

if (22 + d + e) <= 31:
    print("Wielkanoc w roku", year, "wypada:", (22 + d + e), "Marca")
else:
    if d == 29 and e == 6:
        print("Wielkanoc w roku", year, "wypada:", ((d + e - 9) - 7), "Kwietnia")
    if ((d == 28) and (e == 6) and ((m == 2) or (m == 5) or (m == 10) or (m == 13) or (m == 16) or (m == 21) or (m == 24) or (m == 39))):
        print("Wielkanoc w roku", year, "wypada:", ((d + e - 9) - 7), "Kwietnia")
    else:
        print("Wielkanoc w roku", year, "wypada:", (d + e - 9), "Kwietnia")
