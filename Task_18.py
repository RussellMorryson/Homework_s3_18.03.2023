"""Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число 
N – количество элементов в массиве. 

В последующих  строках записаны N целых чисел Ai. 

Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""

N = int(input("Введите размер массива: "))
A = []
for i in range(N):
    Num = int(input(f"Введите {i+1} элемент массива: "))
    A.append(Num)

X = int(input("Введите число, для поиска близкого по величине числа: "))

for j in A:
    if j == X:
        print(j)
    else:
        if X > max(A):
            print(max(A))
            break
        else:
            print(min(A))
            break
