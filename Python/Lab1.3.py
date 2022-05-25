import math

for x in range(15,21):
    result = math.sqrt(math.cos(x) + x ** 4.5)
    print("Result with X = " + (str)(x) + " is: " + (str)(result))
    x += 1