# Zad. 4.2 (0,5 pkt)
# Napisz program generujący N liczb losowych o rozkładzie normalnym (gaussowskim) 
# o zadanych parametrach m (średnia) i σ (odchylenie standardowe) i zapisujący je 
# do pliku binarnego. Następnie plik ten jest odczytywany, liczba po liczbie, 
# a dane zapisywane do nowego pliku (tekstowego), każda liczba w osobnym wierszu.

import matplotlib.pyplot as plt
import numpy as np
from array import array


# mu, sigma, n = 0.5, 0.1, 1000
class Gaussian(object):
    def __init__(self, mu, sigma, n):
        self.mu = mu
        self.sigma = sigma
        self.n = n
        self.s = []
        self.t = []

    # Generate and remove negative values
    def generator(self):
        while len(self.s) < self.n:
            try:
                x = np.random.normal(self.mu, self.sigma, 1)
                assert x > 0
                self.s = np.append(self.s, x)

            except AssertionError:
                self.t = np.append(self.t, x)
        return self.t

    # Save binary file
    def binary_saver(self):
        output_file = open('binary.dat', 'wb')
        float_array = array('d', self.s)
        float_array.tofile(output_file)
        output_file.close()

    # Open binary file and save text file
    def opener_textsaver(self):
        f = open("binary.dat", "r")
        a = np.fromfile(f, dtype=np.float_)
        np.savetxt("text.txt", a, delimiter=",", newline="\n")

    # Prints data
    def printer(self):
        print("\nOdrzucono {} liczb: \n{}\n".format(len(self.t), self.t))
        print(self.s)

    # Create the bins and histogram
    def ploter(self):
        count, bins, ignored = plt.hist(self.s, 30, density=True)

        # Plot the distribution curve
        plt.plot(bins, 1 / (self.sigma * np.sqrt(2 * np.pi)) *
                 np.exp(- (bins - self.mu) ** 2 / (2 * self.sigma ** 2)), linewidth=3, color='r')
        plt.show()


if __name__ == '__main__':
    g = Gaussian(0.5, 0.5, 1000)
    g.generator()
    g.binary_saver()
    g.opener_textsaver()
    g.printer()
    g.ploter()
