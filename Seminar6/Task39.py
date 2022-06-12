# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 
# Вариант 1 Человек с человеком

# total = 50
# while total!=0:
#     a = int(input('Ход первого игрока от 1 до 6 конфет: '))
#     total -= a
#     print(f'Осталось конфет: {total}')
#     if total == 0:
#         print('Первый игрок проиграл!')
#         break
#     b = int(input('Ход второго игрока от 1 до 6 конфет: '))
#     total -= b
#     print(f'Осталось конфет: {total}')
#     if total == 0:
#         print('Второй игрок проиграл!')

# Вариант 2 с ботом
from random import randint

total = int(input('Введите всего конфет: '))
max_step = int(input('Можно брать за один ход конфет: '))

while total != 0:
    if total % (max_step+1) - 1 != 0:
        if total % (max_step+1) == 0:
            take_bot = max_step
        else:
            take_bot = total % (max_step+1) - 1
        total -= take_bot
        print(f'Бот взял {take_bot}')
        print(f'Осталось {total}')
    else:
        take_bot = randint(1,6)
        while take_bot > total:
            take_bot = randint(1,6)
        total -= take_bot
        print(f'Бот взял {take_bot}')
        print(f'Осталось {total}')
        if total == 0:
            print('Бот проиграл')
            break
    take_user = int(input(f'Ход игрока : '))
    while take_user > max_step or take_user > total or take_user < 1:
        take_user = int(input(f'Повторите ввод: '))
    total -= take_user
    print(f'Осталось {total}')
    if total == 0:
        print('Игрок проиграл')
        break