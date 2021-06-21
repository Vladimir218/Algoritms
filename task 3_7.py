# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randrange

x,y = map(int, input('Введите диапазон (x,y) формирования массива чисел: ').split())

a = [0]*(y-x+1)
for i in range(y-x+1):
    a[i] = randrange(x,y)
print(a)

if a[0]<=a[1]:
    min1 = a[0]
    i_min1 = 0
    min2 = a[1]
    i_min2 = 1
else:
    min1 = a[1]
    i_min1 = 1
    min2 = a[0]
    i_min2 = 0

for i in range(2, len(a)):
    if a[i]<min1:
        min2 = min1
        i_min2= i_min1
        min1 = a[i]
        i_min1 = i
    elif a[i]< min2:
        min2 = a[i]
        i_min2 = i
print(f'{min1=} {min2=}')