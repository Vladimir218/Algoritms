# 2.	Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint


def merge_array(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def sort_arr(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = sort_arr(a1)
    if len(a2) > 1:
        a2 = sort_arr(a2)

    return merge_array(a1, a2)


m = int(input(f'Введите размер массива m: '))

arr = [randint(0, 50) for i in range(m)]
print(f'Исходный массив {arr}')

print(f'Отсортированный массив {sort_arr(arr)}')
