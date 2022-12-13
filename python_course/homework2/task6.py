# * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#   (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#   “название”: [“компьютер”, “принтер”, “сканер”],
#   “цена”: [20000, 6000, 2000],
#   “количество”: [5, 2, 7],
#   “ед”: [“шт.”]
# }


item_dict = {'name': None,
             'costs': None,
             'quantity': None,
             'units': None}

# items = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#          (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#          (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
items = []


def show_menu():
    print("\nChoose an option:")
    print("1. New item")
    print("2. Get statistic")
    print("3. Exit")


def input_number_val(top_val=None, menu_text='Choose number: '):
    num = ''
    while type(num) != int:
        try:
            num = int(input(menu_text))
            if num < 0:
                num = ''
                continue
            if top_val is None:
                pass
            elif num > top_val:
                num = ''
                continue
            return num
        except ValueError:
            num = ''


def enter_new_item():
    item_dict = {'name': None,
                 'costs': None,
                 'quantity': None,
                 'units': None}
    for key in item_dict.keys():
        print(f"Enter item {key}: ")
        if (key == 'name' or
                key == 'units'):
            item_dict[key] = input()
        else:
            item_dict[key] = input_number_val()
    tmpobj = (len(items), item_dict)
    items.append(tmpobj)


def print_stat():
    try:
        _, test_dict = items[0]
    except IndexError:
        print('Product list is empty!')
        return

    stat = {}

    for key in test_dict.keys():
        stat[key] = []
    # #slow
    # # for _,dict in items:
    # #   for key in stat.keys():
    # #     if (stat[key].count(dict[key]) == 0):
    # #       stat[key].append(dict[key])

    # faster
    for _, dict in items:
        for key, value in stat.items():
            temp = dict[key]
            if value.count(temp) == 0:
                value.append(temp)
    print(stat)


def chek_command(command):
    if command == 3:
        exit()
    elif command == 2:
        print_stat()
    else:
        enter_new_item()


def main():
    command = 0
    while command != 3:
        show_menu()
        chek_command(input_number_val(3))


if __name__ == '__main__':
    main()
