# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def my_func(name, last_name, years, city, email, tel):
    return f'{name} {last_name}, родился в {years} году, живет в городе {city}, емеил - {email}, телефон - {tel}'


user_name = input('Введите ваше имя')
user_last_name = input('Введите вашу фамилию')
user_years = int(input('Введите ваш год рождения'))
user_city = input('Введите ваш город')
user_email = input('Введите ваш емеил')
user_tel = int(input('Введите ваш телефон'))

print(my_func(name=user_name, last_name=user_last_name, years=user_years,
              city=user_city, email=user_email, tel=user_tel))
