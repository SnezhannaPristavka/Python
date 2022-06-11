# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

path = 'polinom.txt'
f = open(path, 'r')
data = f.read().split()
f.close()

print(data)

path_one = 'polinom_1.txt'
f_one = open(path_one, 'r')
data_one = f_one.read().split()
f.close()
print(data_one)

result = []
sum = 0
duplicate = 0

if len(data) > len(data_one):
    for i in range(0, len(data)):
        if 'x' in data[i] or data[i] == '=':
            for j in range(0, len(data_one)):
                if data[i] == data_one[j]:
                    sum = str(int(data[i-1])+int(data_one[j-1]))
                    result.append(sum + data_one[j])
                    duplicate = 1
                else:
                    uniqum = 1
            if uniqum == 1 and duplicate == 0:
                result.append(data[i-1] + data[i])
                uniqum = 0
            duplicate = 0   
else:
    for i in range(0, len(data_one)):
        if 'x' in data_one[i] or data_one[i] == '=':
            for j in range(0, len(data)):
                if data_one[i] == data[j]:
                    sum = str(int(data_one[i-1])+int(data[j-1]))
                    result.append(sum + data[j])
                    duplicate = 1
                else:
                    uniqum = 1
            if uniqum == 1 and duplicate == 0:
                result.append(data_one[i-1] + data_one[i])
                uniqum = 0
            duplicate = 0

list= ' + '.join(result) + '0'
with open('polynom_sum.txt', 'w') as sum:
    sum.writelines(list)
print(list)