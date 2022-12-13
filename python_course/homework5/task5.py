# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("task5.txt", "w+") as f:
    for x in range(1, 11):
        f.write(str(randint(1, 11)) + ' ')
    f.seek(0)
    print(f"Sum numbers from file: {sum(map(int, f.readline().split()))}")
