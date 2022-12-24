# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input("Ведите натуральное число: "))
list = []
for i in range(2, N+1):
    for j in list:
        if i % j == 0:
            break
    else:
        list.append(i)
print(*list)