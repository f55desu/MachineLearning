import math

def getX():
    pass
def getXi(a, i, h):
    xi = a + i*h
    return xi
def getStep(b, a, n):
    h = (b-a)/n
    return h

def PIntegral (x):
    pi = 1/(x + 1)*math.sqrt(x)

a = int(input("a: "))
b = int(input("b: "))
n = int(input("n: "))


