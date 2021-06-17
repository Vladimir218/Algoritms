'''
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''


def summ(start, n):
    if n == 0:
        return start;
    else:
        return start + summ(start / -2, n - 1);


n = int(input('Введите количество элементов: '));
start = 1;

print(f'{summ(start, n - 1)}');
