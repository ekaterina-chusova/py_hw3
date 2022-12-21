# Задайте список из нескольких чисел. Напишите программу, к
# оторая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input("Введите количество элементов в списке: "))
my_list = []

for i in range(n):
    my_list.append(random.randint(0,10))

print(my_list)    

initial_list = []
sum = 0
for i in range(1, n, 2):
    sum += my_list[i]
    initial_list.append(str(my_list[i]))

print('На нечётных позициях списка стоят элементы ', ', '.join(initial_list), f'. Сумма элементов равна {sum}.') 