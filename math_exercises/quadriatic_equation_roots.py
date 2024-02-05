import math

def quadraticRoots(a: float, b: float, c:float):
    delta = b ** 2- 4*a*c # 0
    if delta < 0:
        return [-1]
    x1 = (-b -math.sqrt(delta)) / (2 * a)
    x2 = (-b +math.sqrt(delta)) / (2 * a)
    final_x1 = math.floor(x1)
    final_x2 = math.floor(x2)
    if final_x1 > final_x2:
        return [final_x1, final_x2]
    return [final_x2, final_x1]


a = float(input("write a:  "))
b = float(input("write b:  "))
c = float(input("write c:  "))

print(quadraticRoots(a, b, c))
