dict = {'Winter/Зима': (1, 2, 12),
        'Sping/Весна': (3, 4, 5),
        'Summer/Лето': (6, 7, 8),
        'Autumn/Осень': (9, 10, 11)}

var = int(input('Введите номер месяца: '))
for key in dict.keys():
    if var in dict [key]:
        print('Вы выбрали время года: ' + key)
