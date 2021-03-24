# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open('task-1.txt', 'w', encoding='utf-8') as my_file:
    while True:
        user_mess = input('Введите то, что хотите записать')
        my_file.write(user_mess)
        if user_mess == '':
            break

