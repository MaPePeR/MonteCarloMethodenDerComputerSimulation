import random
import math

class Experiment:
    def __init__(self, L, D, N):
        assert L <= D
        self.L = L
        self.D = D
        self.N = N

    def werfeNadeln(self):
        n = 0
        for i in range(self.N):
            if (self.werfe()):
                n += 1
        return n

    def werfe(self):
        x = random.uniform(0,self.D)
        winkel = random.uniform(0,math.pi)
        return x < (self.L/2) * math.sin(winkel) or x > self.D - (self.L/2) * math.sin(winkel)

    def pi(self, n = None):
        if n is None:
            n =  self.werfeNadeln()
        if n == 0:
            return 0.
        return 2 * (self.L / self.D) * (self.N / n)

pisum = 0
Ns = [1,2,3,4,5,6]
print("{:>13} {:>13} {:>13}".format("N", "n", "pi"))
for N in map(lambda i: 10**i, Ns):
    e = Experiment(3,10,N)
    n = e.werfeNadeln()
    pi = e.pi(n)
    pisum += pi
    print("{:13,} {:13,} {:13.8f}".format(N, n, pi))
print("Mittelwert pi: {:.8f}\n".format(pisum/len(Ns)))

M = 50
N = 10**5
print("M={} Experimente mit N={}".format(M, "10**5"))
e = Experiment(3,10,N)
ns = []
pis = []
pisum = 0
for i in range(M):
    n = e.werfeNadeln()
    ns.append(n)
    pi = e.pi(n)
    pis.append(pi)
    print("{:>13,} {:>13,} {:>10.8f}".format(N, n, pi))

mittelwert = sum(ns) / len(ns)
varianz = sum(map(lambda x: (x-mittelwert)**2, ns )) / (len(ns) - 1)

print("{:20} {:.8f}\n{:20} {:.8f}".format("Mittelwert von n:", mittelwert, "Varianz von n:", varianz))

mittelwert = sum(pis) / len(pis)
varianz = sum(map(lambda x: (x-mittelwert)**2, pis )) / (len(pis) - 1)
print("{:20} {:.8f}\n{:20} {:.8f}".format("Mittelwert von pi:", mittelwert, "Varianz von pi:", varianz))
