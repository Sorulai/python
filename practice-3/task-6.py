# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
user_text = input('Введите слово или фразу: ')


def int_func(text):
    return text.title()


def int_func1(text):
    new_text = text.split()
    if len(new_text) == 1:
        letter = new_text[0]
        letters = letter[0:1].upper()
        a = letter[1:]
        new_letter = letters + a
        return new_letter
    else:
        list_mask = []
        for el in new_text:
            letter1 = el[0:1].upper()
            a1 = el[1:]
            new_letter1 = letter1 + a1
            list_mask.append(new_letter1)

        return ' '.join(list_mask)


print(int_func(user_text))
print(int_func1(user_text))
