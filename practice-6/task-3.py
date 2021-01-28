# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров)

class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = 'worker'
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):
    def get_full_name(self):
        return f'Содрудника зовут {self.name} {self.surname}'

    def get_total_income(self):
        summ = 0
        for i in self._income.values():
            summ += i
        return f'Доход сотрудника = {summ}'


worker1 = Position(name='Андрей', surname='Петров', wage=25000, bonus=10000)
print(worker1.get_full_name())
print(worker1.get_total_income())

worker2 = Position(name='John', surname='Smit', wage=32500, bonus=15500)
print(worker2.get_full_name())
print(worker2.get_total_income())

worker3 = Position(name='Anastasia', surname='Pitt', wage=41752, bonus=11365)
print(worker3.get_full_name())
print(worker3.get_total_income())
