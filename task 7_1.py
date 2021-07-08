# 1.Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности
# доработайте алгоритм (сделайте его умнее).
from random import randint

def buble_sort(arr):
    n = 1
    cout_sort = -1
    while n < len(arr) and cout_sort != 0:
        cunt_sort = 0
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                cout_sort += 1
        n += 1
    return arr

m= int(input('Введите m для генерации случайного массива размерностью m: '))

numbers = [randint(-100, 100) for i in range(m)]

print (f"Исходный массив {numbers}")
print (f"Отсортированный массив {buble_sort(numbers)}")