import os
import math

def fshift():
    x = os.urandom(1)
    list(x)
    y = x[0]/10
    return math.floor(y)

message = input('Podaj tekst do zaszyfrowania:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
punct = ''' .,:;!?'“”"-()[]{}<>/'''
encrypted, shftLst = [], []

for i in message:
    i = i.lower()
    shift = fshift()
    shftLst.append(shift)
    if i not in punct:
        encrypted.append(alphabet[alphabet.index(i)-(26-shift)])
    else:
        encrypted.append(i)

encrStr = "".join(encrypted)

print(encrStr)
print(shftLst)
