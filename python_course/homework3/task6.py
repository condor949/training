# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(string):
    for i in string.split():
        if i.isalpha():
            for j in i:
                if j.islower():
                    continue
                else:
                    return False
        else:
            return False
    print(string.title())
    return True


def main():
    print('Non compatible format' if int_func(input('Enter string in lower case: ')) is False else '')


if __name__ == '__main__':
    main()
