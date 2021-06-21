
# 3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randrange

x,y = map(int, input('Введите диапазон (x,y) формирования массива чисел: ').split())

a = [0]*(y-x+1)
for i in range(y-x+1):
    a[i] = randrange(x,y)

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

print (f'Первоначальный массив {a=}')
a[i_max],a[i_min] = a[i_min],a[i_max]
print (f'Массив с перестановкой{a}')