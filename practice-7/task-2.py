# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, some__attr):
        self.some_attr = some__attr

    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return round(self.some_attr + other.some_attr, 2)


class Coat(Clothes):
    def __init__(self, some__attr):
        super().__init__(some__attr)

    @property
    def tissue_consumption(self):
        return round(self.some_attr / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, some__attr):
        super().__init__(some__attr)

    @property
    def tissue_consumption(self):
        return round(self.some_attr * 2 + 0.3, 2)


mes1 = int(input('Введите ваш размер одежды'))
mes2 = float(input('Введите ваш рост (например:1.62)'))
coat = Coat(mes1)
suit = Suit(mes2)
print(f'Ткани нужно на пальто = {coat.tissue_consumption}m')
print(f'Ткани нужно на костюм = {suit.tissue_consumption}m')
result = coat.tissue_consumption + suit.tissue_consumption
print(f'Всего ткани нужно = {result}')
