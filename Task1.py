# Вычислить число c заданной точностью d

from math import pi
d = int(input("Ведите количество знаков после запятой от 1 до 10: "))
if 10<d<1:
    print ("Неверное условие!")
else:
    print (round (pi,d))