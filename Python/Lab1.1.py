import math

x1, x2, x3 = 2.5 , -4.4 , 0.001

y1 = math.sin(x1) + 3 * (math.e ** x1)

y2 = math.sin(x2) + 3 * (math.e ** x2)

y3 = math.sin(x3) + 3 * (math.e ** x3)

print("Sin with X = 2.5: " + (str)(y1))

print("Sin with X = -4.4: " + (str)(y2))

print("Sin with X = 0.001: " + (str)(y3))