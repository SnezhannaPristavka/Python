# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
def random_coef(deg_ree):
    random_list = [randint(0,101) for i in range(deg_ree+1)]
    return random_list

def polynomial(list_arg,degree):
    result_list = [str(list_arg[i])+'*x^'+str(degree-i) for i in range(degree) if list_arg[i] != 0]
    if list_arg[-1] != 0:
        result_list.append(str(list_arg[-1])) 
    result = ' + '.join(result_list) + ' = 0'
    return result

k = randint(1,11)
list = random_coef(k)
with open('polinom.txt', 'w') as data:
    data.writelines(polynomial(list,k))
k_1 = randint(1,11)
list_1 = random_coef(k_1)
with open('polinom_2.txt', 'w') as data_1:
    data.writelines(polynomial(list,k))