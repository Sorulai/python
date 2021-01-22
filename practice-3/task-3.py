# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    list_num = [num1, num2, num3]
    list_num.sort(reverse=True)
    list_num.pop()
    return sum(list_num)


print(my_func(1,10,7))