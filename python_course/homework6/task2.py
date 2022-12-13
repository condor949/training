# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

import unittest


class Road:
    __width = 0
    __length = 0
    __mass_asph_per_sq_meter = 25

    def __init__(self, width=20, length=1000):
        self.__width = width
        self.__length = length

    def calculate(self, sheet_thickness):
        return self.__length * self.__width * Road.__mass_asph_per_sq_meter * sheet_thickness


class TestRoad(unittest.TestCase):

    def test_calculate(self):
        road_66 = Road()
        sheet_thickness = [3, 4, 5]
        for x in sheet_thickness:
            if x == 3:
                self.assertEqual(road_66.calculate(x), 1500000, "Should be 1.500.000")
            elif x == 4:
                self.assertEqual(road_66.calculate(x), 2000000, "Should be 2.000.000")
            elif x == 5:
                self.assertEqual(road_66.calculate(x), 2500000, "Should be 2.500.000")
            else:
                self.assert_(False, 'Incorrect test value of sheet thickness')


if __name__ == '__main__':
    unittest.main()
