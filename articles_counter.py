from string import punctuation

s = input('Wprowadź jakiś tekst: \n')
for c in punctuation:
    s = s.replace(c, '')
s = s.lower()
L = s.split()

words = ['a', 'an', 'the']
print()
for item in words:
    article = L.count(item)
    print("Słowo '{}' występuje {} razy.".format(item, article))
