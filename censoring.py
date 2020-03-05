from string import punctuation
sentence = input("Wprowadź zdanie:")

for c in punctuation:
    sentence = sentence.replace(c, ' ' + c)

words = sentence.split()
curse = ['darn', 'dang', 'freakin', 'heck', 'shoot']
censored = []

for word in words:
    if word.lower() in curse:
        word = '*' * len(word)
    censored.append(word)
str_censored = ' '.join(censored)
print(str_censored)
