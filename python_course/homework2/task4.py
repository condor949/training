# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Enter a number of words separated by a space: ')
split_string = string.split()
for i in split_string:
    print(i[:10])
