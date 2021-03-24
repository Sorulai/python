# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
new_list = []
list_numbers_ru = ['Один ', 'Два ', 'Три ', 'Четыре ']
with open('task-4.txt', encoding='utf-8') as my_file:
    for line in my_file:
        new_list.append(line.split())

for i, el in enumerate(new_list):
    el.append('\n')
    el.pop(0)
    el.insert(0, list_numbers_ru[i])

with open('task-4.1.txt', 'w', encoding='utf-8') as my_file:
    for line in new_list:
        my_file.writelines(line)
