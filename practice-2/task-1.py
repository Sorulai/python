# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = [25, 47.3, 'Hello John', [25, 30, 40], ('1', '2', 3), {'name': 'Mike', 'age': 25}]

for el in new_list:
    print(type(el))
