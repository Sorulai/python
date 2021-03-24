# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        """

        :param direction: направление движения
        :return:
        """
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость автомобиля {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышает допустимую скорость'
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} превышает допустимую скорость'
        else:
            return super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


town_car = TownCar(55, 'Green', 'Mazda')
sport_car = SportCar(120, 'White', 'Lamborghini')
work_car = WorkCar(65, 'Yellow', 'Man')
police_car = PoliceCar(60, 'Black', 'BMW')

print(f'name - {town_car.name},цвет - {town_car.color}, полиция? - {town_car.is_police}')
print(town_car.go())
print(town_car.show_speed())
print(town_car.turn('Влево'))
print(town_car.stop())
print('----------')
print(f'name - {sport_car.name},цвет - {sport_car.color}, полиция? - {sport_car.is_police}')
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.turn('Направо'))
print(sport_car.stop())
print('----------')
print(f'name - {work_car.name},цвет - {work_car.color}, полиция? - {work_car.is_police}')
print(work_car.go())
print(work_car.show_speed())
print(work_car.turn('Влево'))
print(work_car.stop())
print('----------')
print(f'name - {police_car.name},цвет - {police_car.color}, полиция? - {police_car.is_police}')
print(police_car.go())
print(police_car.show_speed())
print(police_car.turn('Направо'))
print(police_car.stop())
print('----------')
