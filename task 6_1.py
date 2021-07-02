# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# система 64 бита. Python 3.9.1

import sys

# Оценим память для программы: Урок 3. Задача 1.

a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i % j == 0:
            a[j-2] += 1

for i in range(len(a)):
    print(f'{a[i]} чисел кратно {i+2}')


mamory_size = sys.getsizeof(a)
mamory_size += sys.getsizeof(i)
mamory_size += sys.getsizeof(j)

print(f"Переменные программы занимают {mamory_size} байт")

# Измеренное значение занимаемой памяти - 176 байт, что выше расчетного:
# a = 40 + 8 * 8 = 104 (измеренное - 120, возможно учитывается пвамять на GC)
# i = 24 (измеренное 28)
# j = 24 (измеренное 28)


# Оценим память для программы: Урок 3. Задача 2.
from random import randrange

x,y = map(int, input('Введите диапазон (x,y) формирования массива чисел: ').split())

a = [0]*(y-x+1)
b = []
for i in range(y-x+1):
    a[i] = randrange(x,y)

for i in range(len(a)):
    if a[i] != 0 and a[i]%2 == 0:
        b.append(i)

print(f'В массиве {a} позиции четных элементов - {b}')

mamory_size = sys.getsizeof(x)
mamory_size += sys.getsizeof(y)
mamory_size += sys.getsizeof(a)
mamory_size += sys.getsizeof(b)
mamory_size += sys.getsizeof(i)

print(f"Переменные программы занимают {mamory_size} байт")

# При x=20 у=40 переменные занимают память - 492 байта (измеренное значение)
# a = 40 + 8 * 21 = 208 (измеренное - 224, возможно учитывается пвамять на GC)
# b = 40 + 8 * 8 = 104 (измеренное - 120, возможно учитывается пвамять на GC)
# i = 24 (измеренное 28)
# x = 24 (измеренное 28)
# y = 24 (измеренное 28)

# Оценим память для программы: Урок 3. Задача 3.

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

mamory_size = sys.getsizeof(x)
mamory_size += sys.getsizeof(y)
mamory_size += sys.getsizeof(a)
mamory_size += sys.getsizeof(_min)
mamory_size += sys.getsizeof(_max)
mamory_size += sys.getsizeof(i_min)
mamory_size += sys.getsizeof(i_max)
mamory_size += sys.getsizeof(i)

print(f"Переменные программы занимают {mamory_size} байт")

# При x=20 у=40 переменные занимают память - 420 байта (измеренное значение)