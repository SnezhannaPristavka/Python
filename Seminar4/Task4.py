# Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
import math
m,n=map(int,input('Введите два целых числа через пробел ').split())
print((n * m) // math.gcd(n , m))