# Урок 4. Задача 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках практического задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

'''
Для примера взята задача из Урока2 №4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

В данной задаче написаны два алгоритма решения (с рекурсией и с использованием цикла.
Для двух реализаций оценено время выполнения.
'''
import cProfile


def summ1(start, n):
    s = 0
    for i in range(n):
        s += start
        start = start / -2
    return s


def summ(start, n):
    if n == 0:
        return start
    else:
        return start + summ(start / -2, n - 1)


n = int(input('Введите количество элементов: '))
start = 1

print(cProfile.run("summ(start, n - 1)"))
print(cProfile.run("summ1(start, n)"))

# Оба алгоритма имеют сложность O(n),
# но алгоритм с циклом показывает лучшие показатели по быстродействию чем рекурсия.
# Результаты представленны ниже:
# Для функции summ
#         953 function calls (4 primitive calls) in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#     950/1    0.003    0.000    0.003    0.003 task 4_1.py:24(summ)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# None
#
# Для функции summ1
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task 4_1.py:16(summ1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# None
