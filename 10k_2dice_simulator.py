from random import randint

dsum = []
frequencies = []
perall = []

for i in range(10000):
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    dice_sum = dice1 + dice2
    dsum.append(dice_sum)

for j in range(2,13):
    frequencies.append(dsum.count(j))
fsum = sum(frequencies)
print("Częstotliwość: {} = {}\n".format(frequencies, fsum))

for k in range(len(frequencies)):
    percent = ((frequencies[k]/fsum)*100)
    perall.append(percent)
    print("{:>2} -- {:>5} % {}".format(k+2, round(percent,2), "#"*int(percent)))

print("\nRazem: {}%".format(round(sum(perall))))
