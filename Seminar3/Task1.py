# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Odd_sum(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 !=0:
            sum+=list[i]
    return sum
list = [2, 3, 5, 9, 3]

sum_num = Odd_sum(list)

print(f'Сумма чисел на нечетных позициях в списке равна {sum_num}')