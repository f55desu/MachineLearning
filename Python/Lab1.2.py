import math
import django

x = (float)(input("Enter X: "))
z = (float)(input("Enter Z: "))

y = 15/math.log(x) + math.atan(z/x) * 1/5

print("Y with X = " + (str)(x) + " and Z = " + (str)(z) + " equals: " + (str)(y))