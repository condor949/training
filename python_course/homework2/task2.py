# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

smth_fil_list = []
a = ''
while type(a) != int:
    try:
        a = int(input('Input length list: '))
        if a < 0:
            a = ''
            continue
    except ValueError:
        a = ''

for i in range(a):
    smth_fil_list.append(input('Input element: '))

i = 0
while i < a:
    if i+1 < a:
        smth_fil_list[i], smth_fil_list[i+1] = smth_fil_list[i+1], smth_fil_list[i]
        i=i+2
    if i+1 >= a:
        break

print(smth_fil_list)