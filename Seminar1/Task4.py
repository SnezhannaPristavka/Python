# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
from math import sqrt

def Get_distance(x1,y1,x2,y2):
    x_distance = x2 - x1
    y_distance = y2 - y1

    return sqrt((x_distance**2) + (y_distance**2))

x_first = float(input('Input x of point A: '))
y_first = float(input('Input y of point A: '))
x_second = float(input('Input x of point B: '))
y_second = float(input('Input y of point B: '))

distance = Get_distance(x_first,y_first,x_second,y_second)
print(f'Расстояние между точками равняется {round(distance,2)}')