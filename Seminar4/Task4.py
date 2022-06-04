# Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# b,n=map(int,input().split())
# m=max(b,n)
# while True:
#     if m%b==0 and m%n==0:
#         print(m)
#         break
#     else:
#         m+=1
import math
# n = 16
# m = 12
m,n=map(int,input('Введите два целых числа через пробел ').split())
print((n * m) // math.gcd(n , m))