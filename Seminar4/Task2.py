# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

positive_list = []
negative_list = []
for e in range(1, 9):
    positive_list.append(fib(e))

for i in positive_list:
    negative_list.append(i)

for i in range(len(negative_list)):
    if i % 2 !=0:
        negative_list[i] *= -1
negative_list.reverse()

result = [*negative_list,0,*positive_list]
print(result)