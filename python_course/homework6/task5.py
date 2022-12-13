# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, title="Something draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Just start drawing with Pen! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Just start drawing with Marker! {self.title}')


stat = Stationary()
stat.draw()

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()
