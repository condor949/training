# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task1.txt", "wt") as f:
    string = None
    while string != '':
        string = input('Enter string: ')
        f.write(string+'\n')
