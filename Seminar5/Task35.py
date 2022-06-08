# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

path = 'C:/Users/gorlo/OneDrive/Рабочий стол/Programmist/Python/Homework/number.txt'
f = open(path, 'r')
data = f.read().split()
f.close()

my_list = list(map(int,data))
my_list.sort()

for i in range(1,len(my_list)):
    if my_list[i] - 1 == my_list[i-1]:
        continue
    else:
        find_number = my_list[i] - 1
        
print(find_number)