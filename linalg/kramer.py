import copy
import numpy as np

A = np.array([[2, -1, 5], [1, 1, -3], [2, 4, 1]])
b = np.array([10, -2, 1])

def kramer(A, b):
    detA = np.linalg.det(A)

    print(f'A:\n{A}\n')
    print(f'b:\n{b}\n')

    print(f'det(A): {detA}\n')
    #проверим совместность системы
    if detA != 0:
        print(f'Система совместна и имеет единственное решение\n')
        k = 0
        Ds = []
        #соберем лист определителей с подмененым столбцом
        while k != len(A):
            tmpD = []
            for i,line in enumerate(A):
                tmpD.append(copy.deepcopy(line))
                tmpD[i][k] = b[i]
            Ds.append(copy.deepcopy(tmpD))
            k+=1

        print(Ds)
        #считаем det для каждого определителя из предыдущего списка
        p = [np.linalg.det(np.array(i)) for i in Ds]
        #находим x-сы
        Xs = [i/detA for i in p]
        for i,x in enumerate(Xs):
            print(f'x{i} = {x}\n')
    else:
        print(f'Cистема  несовместна\n')

kramer(A,b)