# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

my_dict = {'profit': 0, 'demages': 0}
profit = {}
average_profit = {}
demage = {}
with open('task-7.txt', encoding='utf-8') as my_file:
    for line in my_file:
        new_str = line.split()
        res = int(new_str[2]) - int(new_str[3])
        if res > 0:
            profit[new_str[0]] = res
            my_dict['profit'] = profit
        else:
            demage[new_str[0]] = res
            my_dict['demages'] = demage

count = 0
average = 0
for k in my_dict['profit'].values():
    average += k
    count += 1

average = round(average / count, 2)
average_profit['average_profit'] = average
my_list = [my_dict, average_profit]

with open('task-7.json', 'w', encoding='utf-8') as j_file:
    json.dump(my_list, j_file)
