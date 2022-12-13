# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from re import split

with open("task3.txt") as f:
    summ = 0
    count = 0
    print([split('\s+', x)[0] for x in f if int(split('\s+', x)[1]) > 20000])
    f.seek(0)
    for _, x in enumerate(f):
        summ += int(split('\s+', x)[1])
        count += 1
    print(f"Average income {summ/count}")
