# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

from random import randrange

x,y = map(int, input('Введите диапазон (x,y) формирования массива чисел: ').split())

a = [0]*(y-x+1)
for i in range(y-x+1):
    a[i] = randrange(x,y)
print(a)

_min = a[0]
_max = a[0]
i_min = 0
i_max = 0

for i in range(1, len(a)):
    if _min > a[i]:
        i_min = i
        _min = a[i]
    elif _max < a[i]:
        i_max = i
        _max = a[i]
s = sum(a[i_min+1:i_max])
print(f'Сумма между максимальным и минимальным элементами - {s}')