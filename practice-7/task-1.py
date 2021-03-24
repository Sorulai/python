# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, new_list):
        self.new_list = new_list

    def __str__(self):
        new_str = ''
        s = ''
        for i in self.new_list:
            for el in i:
                s = s + str(el) + ' '
            new_str = new_str + s + '\n'
            s = ''
        return new_str

    def __add__(self, other):
        my_list = []
        list_mask = []
        res = 0
        for i, el in enumerate(self.new_list):
            for j, num in enumerate(el):
                res = num + other.new_list[i][j]
                list_mask.append(res)
                res = 0
            my_list.append(list_mask)
            list_mask = []

        return Matrix(my_list)


my_list1 = [[2, 4, 5], [3, 7, 4], [9, 4, 5]]
my_list2 = [[3, 4, 5], [5, 8, 7], [2, 7, 7]]
my_list3 = [[1, 5, 6], [4, 1, 2], [2, 4, 3]]
matrix1 = Matrix(my_list1)
matrix2 = Matrix(my_list2)
matrix3 = Matrix(my_list3)
print(matrix1)
print(matrix2)
print(matrix3)
print(matrix1 + matrix2 + matrix3)
