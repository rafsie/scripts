encmes = input('Podaj zaszyfrowany tekst:')
strkey = eval(input('Podaj klucz jako listę:'))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
punct = ''' .,:;!?'“”"-()[]{}<>/'''
decrypted, key, shift = [], [], []

for i in strkey:
    key.append(i)

for j in range(0, len(encmes)):
    if encmes[j] not in punct:
        decrypted.append(alphabet[alphabet.index(encmes[j]) - (key[j])])
    else:
        decrypted.append(encmes[j])

decrStr = "".join(decrypted)
print(decrStr)
