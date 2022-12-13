# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
import unittest


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


class TestPosition(unittest.TestCase):
    def test_calculate(self):
        workers = [Position('Thomas', 'Anderson', 'programmer', 10000, 5000),
                   Position('Elliot', 'Anderson', 'security engineer', 15000, 2000),
                   Position('Deon', 'Wilson', 'android developer', 13000, 3000)]
        for val in workers:
            if val.position == 'programmer':
                self.assertEqual(val.get_full_name(), 'Thomas Anderson', "Should be Thomas Anderson")
                self.assertEqual(val.get_total_income(), 15000, "Should be 15.000")
            elif val.position == 'security engineer':
                self.assertEqual(val.get_full_name(), 'Elliot Anderson', "Should be Elliot Anderson")
                self.assertEqual(val.get_total_income(), 17000, "Should be 17.000")
            elif val.position == 'android developer':
                self.assertEqual(val.get_full_name(), 'Deon Wilson', "Should be Deon Wilson")
                self.assertEqual(val.get_total_income(), 16000, "Should be 16.000")
            else:
                self.assert_(False, 'Incorrect test data')


if __name__ == '__main__':
    unittest.main()
