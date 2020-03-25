# Zad. 3. (1 pkt)
# Napisz program wczytujący z wiersza poleceń liczbę całkowitą 3-cyfrową,
# z opcjonalnym znakiem '-' (minus) na początku, wypisujący słownie tę liczbę
# (w języku polskim, ale w stylu 'cyfra po cyfrze') na komponencie typu. Przykłady:

# 127 -> jeden dwa siedem
# -205 -> minus dwa zero pięć
# 911 -> dziewięć jeden jeden

# Próba wczytania niedozwolonej liczby, tj. o innej liczbie cyfr niż 3, powinna rzucać
# stosowny wyjątek i w konsekwencji (w kodzie obsługi wyjątku) komunikat o błędzie.
# Wskazówka: w odpowiedni sposób użyj słownika/-ów (np. HashMap<…>).


class Error(Exception):
    pass


class DifferValue(Error):
    pass


class SignBefore(Error):
    pass


numsdict = {1:'jeden', 2:'dwa', 3:'trzy', 4:'cztery',
            5:'pięć', 6:'sześć', 7:'siedem', 8:'osiem',
            9:'dziewięć', 10:'dziesięć', '-':'minus'}

str = ''

number = input('Podaj liczbę trzycyfrową: ')

try:
    if sum(c.isalpha() for c in number) == 0 and sum(c.isdigit() for c in number) != 3:
        raise DifferValue

    if '-' in number and number.index('-') != 0:
        raise SignBefore

    for i in number:
        if i.isnumeric():
            str += numsdict[int(i)] + ' '
        else:
            str += numsdict[i] + ' '

except KeyError:
    print("To nie jest poprawna liczba!")
    exit()

except DifferValue:
    print("Liczba cyfr różna od 3!")
    exit()

except SignBefore:
    print("Umieść znak przed liczbą!")
    exit()

print(str)
