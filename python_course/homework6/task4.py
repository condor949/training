# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import unittest


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    @staticmethod
    def go():
        return 'Squeal of tires!'

    @staticmethod
    def stop():
        return 'brake whistle'

    @staticmethod
    def turn(direction):
        return 'turn ' + direction

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.name +' Slow down! Speed limit 60')
            return 60
        return self.speed


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.name + ' Slow down! Speed limit 40')
            return 40
        return self.speed


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TestCars(unittest.TestCase):
    def test_move(self):
        cars = [SportCar('TESLA', 'white', 180),
                PoliceCar('FORD', 'black', 120, True),
                WorkCar('FORD', 'dark red', 60),
                TownCar('Nissan', 'purple', 70)]
        for car in cars:
            self.assertEqual(car.go(), 'Squeal of tires!', "Should be 'Squeal of tires!'")
            self.assertEqual(car.stop(), 'brake whistle', "Should be 'brake whistle'")
            self.assertEqual(car.turn('right'), 'turn right', "Should be 'turn right'")

    def test_speed(self):
        sport = SportCar('TESLA', 'white', 180)
        police = PoliceCar('FORD', 'black', 120, True)
        work = WorkCar('FORD', 'dark red', 60)
        town = TownCar('Nissan', 'purple', 70)
        self.assertEqual(sport.show_speed(), 180, "Should be 180")
        self.assertEqual(police.show_speed(), 120, "Should be 120")
        self.assertTrue(police.is_police, "Should be True")
        self.assertEqual(work.show_speed(), 40, "Should be 40")
        self.assertEqual(town.show_speed(), 60, "Should be 60")

    def test_rights(self):
        sport = SportCar('TESLA', 'white', 180)
        police = PoliceCar('FORD', 'black', 120, True)
        work = WorkCar('FORD', 'dark red', 60)
        town = TownCar('Nissan', 'purple', 70)
        self.assertFalse(sport.is_police, "Should be False")
        self.assertTrue(police.is_police, "Should be True")
        self.assertFalse(work.is_police, "Should be False")
        self.assertFalse(town.is_police, "Should be False")


if __name__ == '__main__':
    unittest.main()
