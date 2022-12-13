# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def divide_and_pour(first, second):
    try:
        return first/second
    except ZeroDivisionError:
        print('There is no spoon.')
        return 0


def input_number_val(menu_text):
    num = ''
    while type(num) != int:
        try:
            num = int(input(menu_text))
            return num
        except ValueError:
            num = ''


def main():
    print(f"Quotient of two numbers: ", divide_and_pour(
        input_number_val('Enter first number: '),
        input_number_val('Enter second number: ')
    ))


if __name__ == '__main__':
    main()
