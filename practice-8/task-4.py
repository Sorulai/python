# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.
from abc import ABC, abstractmethod


class CountErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class WareHouse:
    warehouse = {}

    @classmethod
    def to_take(cls, *some_obj):
        """
        Функция для формирования общего словаря склада из отдельных словарей оргтехники
        """
        for obj in some_obj:
            if isinstance(obj, Printer):
                cls.warehouse['Принтер'] = obj.office_printers
            elif isinstance(obj, Scanner):
                cls.warehouse['Сканер'] = obj.office_scan
            elif isinstance(obj, Coppier):
                cls.warehouse['Ксерокс'] = obj.office_cop

        return cls.warehouse

    @classmethod
    def add_to_firm(cls, name, model, quan):
        """
        Функция передачи техники фирме.
        """
        try:
            if model in cls.warehouse[name]:
                num = cls.warehouse[name][model]['кол-во']
                if quan == num:
                    cls.warehouse[name][model] = 'Нет в наличии'
                elif quan > num:
                    raise CountErr('На складе меньше товара, чем вы хотите приобрести')
                else:
                    num = num - quan
                    cls.warehouse[name][model]['кол-во'] = num
        except CountErr as err:
            print(err)
        finally:
            return cls.warehouse


class OfficeTech(ABC):
    def __init__(self, model, price, quantity):
        self.model = model
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f' {self.model}, кол-во -{self.quantity}, цена за шт-{self.price}'

    @abstractmethod
    def to_send(self):
        '''
        Функция для создания словаря каждого из потомков класса.

        '''
        pass


class Printer(OfficeTech):
    office_printers = {}

    def __init__(self, model, price, quantity, year):
        super().__init__(model, price, quantity)
        self.year = year

    @property
    def to_send(self):
        self.office_printers[self.model] = {
            'кол-во': self.quantity,
            'цена за шт': self.price,
            'год выпуска': self.year

        }
        return self.office_printers


class Scanner(OfficeTech):
    office_scan = {}

    def __init__(self, model, price, quantity, is_colored=False):
        super().__init__(model, price, quantity)
        self.is_colored = is_colored

    @property
    def to_send(self):
        self.office_scan[self.model] = {
            'кол-во': self.quantity,
            'цена за штуку': self.price,
            'Цветной или нет': self.is_colored
        }
        return self.office_scan


class Coppier(OfficeTech):
    office_cop = {}

    def __init__(self, model, price, quantity, series):
        super().__init__(model, price, quantity)
        self.series = series

    @property
    def to_send(self):
        self.office_cop[self.model] = {
            'кол-во': self.quantity,
            'цена за штуку': self.price,
            'серия': self.series
        }
        return self.office_cop


print('Создание экземпляров классов и формирование словарей')
printer1 = Printer('HP752', 7856, 3, 2015)
print(printer1.to_send)
printer2 = Printer('HP5698', 5482, 4, 2020)
print(printer2.to_send)
printer3 = Printer('Acer90', 5214, 5, 2019)
print(printer3.to_send)
scan1 = Scanner('Acer74J', 7452, 10, True)
print(scan1.to_send)
scan2 = Scanner('HPJK90', 6524, 1)
print(scan2.to_send)
cop = Coppier('Xerox89', 4126, 15, 2)
print(cop.to_send)
print('----------------------')
print('Формирование склада:')
print(WareHouse.to_take(printer3, scan2, cop))
ware_dict = WareHouse.to_take(printer3, scan2, cop)
print('На складе есть такие позиции:')
for i, item in ware_dict.items():
    print(f'{i} :')
    for k, i in item.items():
        print(f'{k} {i}  \n')
while True:
    name = input('Введите тип техники:')
    model = input('Введите модель:')
    count = int(input('Введите кол-во'))
    if name not in ['Принтер', 'Сканер', 'Ксерокс']:
        name = input('Такой техники нет на складе, введите еще раз:')
    elif model not in ware_dict[name]:
        model = input('Такой модели нет, посмотрите еще раз на наличии склада:')
    elif count <= 0:
        count = int(input('Вы ввели неверное кол-во, попробуйте еще раз'))
    else:
        print(WareHouse.add_to_firm(name, model, count))
        break
