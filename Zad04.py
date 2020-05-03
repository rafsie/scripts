# Zad. 2.1 (1.5 pkt)
# Zaimplementuj funkcje double LevQWERTY(String s1, String s2), która zwraca ważoną
# odległość Levenshteina miedzy napisami s1 i s2, gdzie wagi zależne są od wzajemnego
# położenia pary znaków na klawiaturze. Konkretniej, odl. Levenshteina bazuje na 3
# elementarnych operacjach: wstawienia znaku (ang. insertion), usuniecia znaku
# (ang. deletion) oraz zastapienia znaku innym (ang. substitution). W naszym przypadku
# waga operacji insercji i delecji ma wynosic 1, natomiast waga substytucji wynosi: 0.5,
# jesli odnośna para znaków sasiaduje w rzedzie na klawiaturze, 1 w przeciwnym przypadku.
# Zakładamy, że s1 i s2 mogą zawierać tylko małe litery łacińskie.
# Przykłady: LevQWERTY("kot", "kita") == 1.5, LevQWERTY("drab", "dal") == 2


def levqwerty(s1, s2):

    key_row = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
               'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
               'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}

    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                if key_row[s1[i]] == key_row[s2[j]]:
                    cost = 0.5
                else:
                    cost = 1

            d[(i,j)] = min(
                           d[(i-1,j)] + 1,
                           d[(i,j-1)] + 1,
                           d[(i-1,j-1)] + cost,
                          )

            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost)

    return d[lenstr1-1,lenstr2-1]
