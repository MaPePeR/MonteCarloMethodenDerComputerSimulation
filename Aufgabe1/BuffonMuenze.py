import random

#Durchmesser Münze
D = 8
R = D/2
#Kantenlänge des Quadratgitters
L = 8

def anzahlBedeckungen(x, y):
    c = 0
    if L <= x + R :
        c += 1
    if x - R <= 0:
        c += 1
    if L <= y + R:
        c += 1
    if y - R <= 0:
        c += 1
    return c

for N in map(lambda i: 10**i, [1,2,3,4,5,6]):
    d = {0:0, 1:0, 2:0, 3:0, 4:0}
    for i in range(N):
        x = random.uniform(0, L)
        y = random.uniform(0, L)
        n = anzahlBedeckungen(x,y)
        d[n] += 1
    print ("{0:8} {1[0]:8} {1[1]:8} {1[2]:8} {1[3]:8} {1[4]:8}".format(N, d))
