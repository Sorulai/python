# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{self.title} рисует тонкие ровные линии синего цвета'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} рисует рванные штрихи серого цвета'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} рисует толстые линии черного цвета'


stationery = Stationery('Канцелярия')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
marker = Handle('Маркер')

print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(marker.draw())
