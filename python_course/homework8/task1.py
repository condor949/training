# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    content = {'day': None,
               'month': None,
               'year': None}

    raw_epoch_time = '01-01-1973'

    def __init__(self, data_str):
        tmp = data_str.split('-')
        for num, key in enumerate(self.content.keys()):
            self.content[key] = int(tmp[num])

    @classmethod
    def extract(cls):
        return [int(x) for x in cls.raw_epoch_time.split('-')]

    @staticmethod
    def validate(data_str):
        for num, val in enumerate(map(int, data_str.split('-'))):
            if num == 0:
                if val > 31 or val < 0:
                    print('Incorrect day in ', data_str)
            elif num == 1:
                if val > 12 or val < 0:
                    print('Incorrect month in ', data_str)
            elif num == 2:
                if val > 3000 or val < 0:
                    print('Incorrect year in ', data_str)


def main():
    v = Data('20-12-2012')
    print(v.content)
    print(v.extract())
    v.validate('32-12-3001')


if __name__ == '__main__':
    main()
