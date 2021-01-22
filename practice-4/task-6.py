# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle


def gen(num1, num2):
    for el in count(num1):
        if el > num2:
            break
        else:
            yield el


user_num1 = int(input('Введите первое число, с которого хотите начать отсчет: '))
user_num2 = int(input('Введите второе число, на котором хотите остановится: '))
res1 = gen(user_num1, user_num2)
for el in res1:
    print(el)

new_list = [10, 25, 30, 45, 50]


def gen2(num1):
    c = 0
    for el in cycle(new_list):
        if c == num1:
            break
        else:
            yield el
        c += 1


user_num3 = int(input('Введите число, сколько раз вы хотите повторять элементы списка: '))
res2 = gen2(user_num3)
for el in res2:
    print(el)