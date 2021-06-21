# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
def min_col(a,x,j):
    _min = a[0][j]
    for i in range(1,x):
        if _min > a[i][j]:
            _min = a[i][j]
    return _min
from random import randrange

x,y = map(int, input('Введите размер матрицы X x Y: ').split())

a = []

for i in range(x):
    b=[]
    for j in range(y):
        b.append(randrange(0,100))
    a.append(b)

print(f'{a=}')

b=[]
for j in range(y):
    b.append(min_col(a,x,j))

print(f'Максимальное значение среди минимальных значений в стлолбцах - {max(b)}')
