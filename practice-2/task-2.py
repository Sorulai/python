# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_flag = True
new_list = []

while my_flag:
    a = input('Введите число или значение(если захотите прервать ввод,нажмите x):')
    if a.lower() == 'x' or a.lower() == 'х':
        my_flag = False
    else:
        new_list.append(int(a))

print(new_list)
my_list = []
i = 0
a = 0
x = new_list.copy()
while True:
    if len(new_list) % 2 == 0:
        my_list.append(new_list[i + 1])
        my_list.append(new_list[i])
        i += 2
        if len(new_list) == len(my_list):
            break
    else:
        a = new_list.pop()

if len(x) != len(my_list):
    my_list.append(a)

print(my_list)
