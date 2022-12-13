# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(first, second, third):
    first_max = second if first < second else first
    second_max = second if third < second else third
    if first_max == second_max:
        second_max = third if first < third else first
    print(first_max + second_max)


def input_number_val(menu_text):
    num = ''
    while type(num) != int:
        try:
            num = int(input(menu_text))
            return num
        except ValueError:
            num = ''


def main():
    my_func(input_number_val('Enter first number: '),
            input_number_val('Enter second number: '),
            input_number_val('Enter third number: '))


if __name__ == '__main__':
    main()
