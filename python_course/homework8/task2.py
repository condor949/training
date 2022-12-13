# Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
from exceptions import ZeroDivision


class Division:
    def __init__(self, val):
        self.val = val

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivision("You can not division on zero")
        else:
            return self.val/other


def main():
    try:
        a = Division(int(input("Input dividend: ")))
        b = int(input("Input divider: "))
        print('solution '+str(a/b))
    except ValueError:
        print("Error type of value!")
    except ZeroDivision as zd:
        print(zd)


if __name__ == '__main__':
    main()
