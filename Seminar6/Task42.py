# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

from encodings.utf_8 import encode

path = 'input_data.txt'
f = open(path, 'r', encoding='utf-8')
data = list(f.read())
f.close()

def coding(list):
    info = open('out_data.txt', 'a', encoding='utf-8')
    cout = 1
    for i in range(0, len(list)-1):
        if list[i] == list[i + 1]:
            cout += 1
        else:
            info.writelines(str(cout))
            info.writelines(list[i])
            cout = 1

    info.writelines(str(cout))
    info.writelines(list[-1] + '\n')
    info.close()


def decoding(list):
    info = open('out_data.txt', 'a', encoding='utf-8')
    for i in range(0,len(list)-1,2):
        new_str = int(list[i]) * list[i+1]
        info.writelines(new_str)
    info.writelines('\n')
    info.close()

choice = int(input('Введите цифру 1 для кодирования или 2 для декодирования ' ))

if choice == 1:
    coding(data)
elif choice == 2:
    decoding(data)
else:
    print('Введены неверные данные!')