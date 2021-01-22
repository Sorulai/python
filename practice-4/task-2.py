# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 555]


def generate(my_list):
    new_list = []
    for i, el in enumerate(my_list):
        try:
            if el < my_list[i + 1]:
                new_list.append(my_list[i + 1])
        except IndexError:
            if my_list[-1] > my_list[i]:
                new_list.append(my_list[-1])
            break

    yield new_list


res = generate(my_list)

for el in res:
    print(el)
