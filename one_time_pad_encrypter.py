from random import randint

message = input('Podaj tekst do zaszyfrowania:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
punct = ''' .,:;!?'“”"-()[]{}<>/'''
encrypted, shftLst = [], []

for i in message:
    i = i.lower()
    shift = randint(0,25)
    shftLst.append(shift)
    if i not in punct:
        encrypted.append(alphabet[alphabet.index(i)-(26-shift)])
    else:
        encrypted.append(i)

encrStr = "".join(encrypted)

print(encrStr)
print(shftLst)
