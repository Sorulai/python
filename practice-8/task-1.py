# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def num_date(cls, date):
        date_list = []
        for i in date.split('-'):
            date_list.append(int(i))

        return date_list[0], date_list[1], date_list[2]

    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year > 0:
                    return f'Все правильно'
                else:
                    return f'Год введен не верно'
            else:
                return f'Месяц введен не верно'
        else:
            return f'День введен не верно'

    def __str__(self):
        return f'Дата {Date.num_date(self.date)}'


user_date = input('Введите дату формата день-месяц-год:')
date = Date(user_date)
print(date)
print(Date.num_date(user_date))
print(Date.valid_date(11, 5, 2021))
print(Date.valid_date(13, 13, 2021))
