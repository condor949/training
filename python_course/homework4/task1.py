# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import argparse


def createParser():
    parser = argparse.ArgumentParser(
        prog='payroll',
        description='''The program allows you to calculate the salary of an employee for any period''',
        epilog='''(c) condor949 2021. Because i can.''',
        add_help=False)
    payroll_group = parser.add_argument_group(title='Параметры')
    payroll_group.add_argument('-p', '--production', type=int, default=160, help='Time worked by the employee for the '
                                                                                 'target period', metavar='Hour')
    payroll_group.add_argument('-r', '--rate', type=int, default=200, help='The rate of a specialist for this '
                                                                           'position per hour', metavar='c.u. per hour')
    payroll_group.add_argument('-b', '--buns', type=int, default=15000, help='The amount of the bonus characteristic '
                                                                             'of this position', metavar='c.u.')
    payroll_group.add_argument('--help', '-h', action='help', help='Справка')
    return parser


def main():
    global namespace
    print(namespace.production*namespace.rate+namespace.buns)


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    main()
