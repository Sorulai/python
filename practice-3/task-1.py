# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(num1, num2):
    try:
        res = num1 / num2
        return res
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


user_number1 = int(input('Введите первое число: '))
user_number2 = int(input('Введите второе число: '))
result = my_func(user_number1, user_number2)
print(result)