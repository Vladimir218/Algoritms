# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randrange
dic = {}
x,y = map(int, input('Введите диапазон (x,y) формирования массива чисел: ').split())

a = [0]*(y-x+1)
for i in range(y-x+1):
    a[i] = randrange(x,y)
print(a)
_max =""
for i in range(len(a)):
    if a[i] < 0:
        if _max == "":
            _max = a[i]
            i_max = i
        elif _max < a[i]:
            _max = a[i]
            i_max = i
if _max == "":
    print('В массиве отрицательных чисел нет')
else:
    print(f'Максимальный отрицательный элемент {_max} находится на позиции {i_max}')