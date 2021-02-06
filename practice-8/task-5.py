# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма - {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        num1 = self.a * other.a - self.b * other.b
        num2 = self.a * other.b + self.b * other.a
        if num2 < 0:
            return f'Умножение = {num1}{num2}i'
        else:
            return f'Умножение = {num1} + {num2}i'

    def __str__(self):
        if self.a == 0:
            return f'Вы ввели число {self.b}i'
        elif self.b == 0:
            return f'Вы ввели число {self.a}'
        elif self.b < 0:
            return f'Вы ввели число {self.a}{self.b}i'
        else:
            return f'Вы ввели число {self.a}+{self.b}i'


cn1 = ComplexNumber(1, -3)
cn2 = ComplexNumber(4, 5)

print(cn1)
print(cn2)
print(cn1 + cn2)
print(cn1 * cn2)
