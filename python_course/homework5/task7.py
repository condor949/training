# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
from re import findall
from json import dump

new_dict = {}
avg_count = 0


def collect_dict(*args):
    global avg_count
    tmp = int(args[1]) - int(args[2])
    new_dict[args[0]] = tmp
    if tmp > 0:
        avg_count += 1
        return tmp
    else:
        return 0


def main():
    global avg_count
    with open("task7.txt") as fr, open("task7.json", "w") as fw:
        dump([new_dict,
                   {'average_profit': round(sum(
                       [collect_dict(*y) for y in [findall("(\w+\S\d)", x) for x in fr]]) / avg_count, 1)}],
                  fw, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()


