# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal = int(input('Введите число: '))

binary_code = []

num = decimal
while num != 0:
    if num % 2 == 0:
        binary_code.insert(0, 0)
    else:
        binary_code.insert(0, 1)
    num = int(num / 2)

print(decimal, '->' , ''.join(map(str,binary_code)), end='')


