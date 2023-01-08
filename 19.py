import math

def area_herao(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))

print(area_herao(18, 23, 31))