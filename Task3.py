# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint
n = int(input("Ведите количество элементов списка: "))
numbers = []
for i in range(n):
    numbers.append(randint(0, 10))
print (numbers)
unique_list = [i for i in set(numbers) if numbers.count(i) == 1]
print(unique_list)


