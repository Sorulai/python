# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

with open('task-5.txt', 'w', encoding='utf-8') as my_file:
    for el in range(5):
        my_file.write(str(random.randint(1, 10)))
        my_file.write(' ')

with open('task-5.txt', encoding='utf-8') as my_file:
    new_list = my_file.read().split()
    res = 0
    for el in new_list:
        res += int(el)
    print(f'Сумма элементов = {res}')
