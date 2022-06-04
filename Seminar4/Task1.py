# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def binarize(num):
    res = 0
    list = []
    while num != 0:
        res = num % 2
        num //= 2
        list.append(res)
    list.reverse()
    return list

number = int(input('Введите число, которое нужно преобразовать '))

binary_list = binarize(number)

for i in binary_list:
    print(i,end='')