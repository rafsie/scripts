# Asterisks censoring program keeping the size of characters and punctuation marks.
# Sample sentence: Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.

sentence = input("Enter the sentence:")

curse = ['darn', 'dang', 'freakin', 'heck', 'shoot']

for word in curse:
    if word in sentence.lower():
        word_index = sentence.lower().index(word)
        sentence = sentence.replace((sentence[word_index:word_index + len(word)]), "*" * len(word))

print(sentence)
