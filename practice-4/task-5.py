# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
import functools

new_list = [el for el in range(100, 1000) if el % 2 == 0]


def my_func(el, next_el):
    return el * next_el


res = functools.reduce(my_func, new_list)
print(res)
