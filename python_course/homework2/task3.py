# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = ('winter', 'spring', 'summer', 'autumn')
year = {seasons[0]: [12, 1, 2],
        seasons[1]: [3, 4, 5],
        seasons[2]: [6, 7, 8],
        seasons[3]: [9, 10, 11]}
a = ''
while type(a) != int:
    try:
        a = int(input('Input correct month number: '))
        if a < 1 or a > 12:
            a = ''
            continue
    except ValueError:
        a = ''
for season, month_list in year.items():
    for month_n in month_list:
        if a == month_n:
            print(season)
