# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# def find_unique(list):
#     new_list = []
#     for i in list:
#         if mylist.count(i) > 1:
#             continue
#         else:
#             new_list.append(i)
#     return new_list
# print(find_unique(mylist))

my_list = list(filter(lambda i : not my_list.count(i) > 1,my_list))
print(my_list)