# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

num = int(input('Введите число: '))

fibbonaci = []

fibbonaci.append(0)
fibbonaci.append(1)
fibbonaci.insert(0, 1)

for i in range(3, num * 2, 2):
    fibbonaci.append(fibbonaci[i-1] + fibbonaci[i-2])
    fibbonaci.insert(0, (fibbonaci[i] * (-1) ** int(i/2)))

print(f'Для k = {num} ряд чисел Фибоначчи и Негафибоначчи будет выглядеть так: {fibbonaci}')