# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, 
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input("Введите количество элементов в списке: "))
my_list = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(n):
    my_list.append(round(random.uniform(0, 10), 2))

# my_list = [1.1, 1.2, 3.1, 5, 10.01]    

new_list = []
for i in range(len(my_list)):
    if (my_list[i] % 1 != 0):
        new_list.append((round(my_list[i] % 1, 2)))

print(f'{my_list} => {max(new_list)-min(new_list)}')