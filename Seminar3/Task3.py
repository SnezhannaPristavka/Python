# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.02, 10.01] => 0.19
import math

def Creat_float_list(list):
    list_new = []
    for i in list:
        list_new.append(round(i % 1, 2))
    return list_new

def Find_diff_max_min(list):
    diff = max(list) - min(list)
    return diff

list = [1.1, 1.2, 3.1, 5.02, 10.01]

float_list = Creat_float_list(list)
difference = Find_diff_max_min(float_list)

# print(float_list) 

print(f'Разница между max и min дробной части списка {list} => {difference}')