# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class complex:
    def __init__(self, x, y):
        self.re = x
        self.im = y

    def __add__(self, other):
        return complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)

    def __repr__(self):
        return '(%f , %f)' % (self.re, self.im)
