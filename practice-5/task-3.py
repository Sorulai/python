# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import statistics
with open('task-3.txt', encoding='utf-8') as my_file:
    my_list = []
    for line in my_file:
        my_list.append(int(line.split()[1]))
        if int(line.split()[1]) < 20000:
            print(f'Оклад меньше 20000 - {line.split()[0]}')

    res = statistics.mean(my_list)
    print(f'Средняя величина зарплаты = {res}')

