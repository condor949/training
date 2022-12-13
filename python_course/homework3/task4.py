# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def input_number_val(menu_text, sign_indicator=1):
    num = ''
    while type(num) != int:
        try:
            num = int(input(menu_text))
            if sign_indicator < 0:
                if num > 0:
                    num = ''
                    continue
                else:
                    return num
            else:
                if num < 0:
                    num = ''
                    continue
                else:
                    return num
        except ValueError:
            num = ''


# Simple try
# def my_func(x, y):
#     return x ** y

# Hard try
def my_func(x, y):
    composition = 1
    if x == 0:
        return composition

    for i in range(1, abs(y)+1):
        composition *= x
    return 1/composition


def main():
    print(my_func(input_number_val('Enter positive basis number: '),
                  input_number_val('Enter negative indicator number: ', -1)))


if __name__ == '__main__':
    main()
