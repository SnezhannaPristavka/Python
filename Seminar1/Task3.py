# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти '))
if quarter > 0 and quarter < 5:
    match quarter:
        case 1:
            print('Точки находятся в диапазоне X > 0 и Y > 0')
        case 2:
            print('Точки находятся в диапазоне X < 0 и Y > 0')
        case 3:
            print('Точки находятся в диапазоне X < 0 и Y < 0')
        case 4:
            print('Точки находятся в диапазоне X > 0 и Y < 0')
else:
    print('Введены неверные данные')