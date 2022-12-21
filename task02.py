# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите количество элементов в списке: "))
my_list = []

for i in range(n):
    my_list.append(random.randint(0,10))

if (n % 2 == 0):
    median = n / 2
else:
    median = ((n + 1) / 2)

new_list = []
for i in range(int(median)):
    new_list.append(my_list[i] * my_list[len(my_list)-1-i])

print(f'{my_list} => {new_list}')