# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

k1 = int(input("Ведите значение степени: "))
from random import randint 
a1=(randint(0, 101))
b1=(randint(0, 101))
c1=(randint(0, 101))
polynomial = [f"{a1}*x^{k1}+{b1}*x+{c1}"]
with open ('file1.txt', 'w') as data:
     data.write(" + ".join(polynomial) + " = 0")

with open('file.txt', "r") as file_one:
     polynomial1=file_one.readline()
     polynomial1=polynomial1.split('=')[0]
     print(polynomial1)
with open('file1.txt', "r") as file_second:
     polynomial2=file_second.readline()
     polynomial2=polynomial2.split('=')[0]
     print(polynomial2)

a, b, c  = polynomial1.split('+')
a = int(a[:a.index('*x')])
b=int(b[:b.index('*x')])
c=int(c)

a1, b1, c1 = polynomial2.split('+')
a1 = int(a1[:a1.index('*x')])
b1=int(b1[:b1.index('*x')])
c1=int(c1)

with open('sum_poly.txt', 'w') as file:
     file.write(f'{(a+a1)}*x^2+{b+b1}*x+{c+c1}')
print(f'{(a+a1)}*x^2+{b+b1}*x+{c+c1}')