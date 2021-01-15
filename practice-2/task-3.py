# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

mounth = int(input('Введите номер месяца: '))

mounth_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

if mounth in mounth_list[0]:
    print('Месяц: Зима')
elif mounth in mounth_list[1]:
    print('Месяц: Весна')
elif mounth in mounth_list[2]:
    print('Месяц: Лето')
elif mounth in mounth_list[3]:
    print('Месяц: Осень')
else:
    print('Такого месяца не существует')

mounth_dict = {'Зима': [12, 1, 2],
               'Весна': [3, 4, 5],
               'Лето': [6, 7, 8],
               'Осень': [9, 10, 11]}

if mounth in mounth_dict.get('Зима'):
    print('Месяц: Зима')
elif mounth in mounth_dict.get('Весна'):
    print('Месяц: Весна')
elif mounth in mounth_dict.get('Лето'):
    print('Месяц: Лето')
elif mounth in mounth_dict.get('Осень'):
    print('Месяц: Осень')
else:
    print('Такого месяца не существует')
