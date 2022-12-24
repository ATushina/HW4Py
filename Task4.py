#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

k = int(input("Ведите значение степени: "))
from random import randint 
a=(randint(0, 101))
b=(randint(0, 101))
c=(randint(0, 101))
print (a,b,c)
print (f"{a}*x^{k}+{b}*x+{c} = 0")
polynomial = [f"{a}*x^{k}+{b}*x+{c}"]
with open ('file.txt', 'w') as data:
     data.write(" + ".join(polynomial) + " = 0")