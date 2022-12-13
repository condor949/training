# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from re import findall


counter = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task4.txt") as f1, open("task4-1.txt", "wt", encoding='utf-8') as f2:
    for x in f1:
        for key, val in counter.items():
            line = findall('\w+', x)
            if line[0] == key:
                f2.write(val + ' - ' + line[1]+'\n')
