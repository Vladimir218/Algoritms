# 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.

from collections import deque

hex16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
         'd': 13, 'e': 14, 'f': 15}
hex10 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
         13: 'd', 14: 'e', 15: 'f'}


def summ(a, b, hex16, hex10):
    if len(a) < len(b):
        a, b = b, a
    rez = deque(a)

    t = 0
    for i in range(len(a)):
        if i <= len(b) - 1:
            temp_s = hex16[a[-i - 1]] + hex16[b[-i - 1]] + t
        else:
            temp_s = hex16[a[-i - 1]] + t

        if temp_s > 15:
            t = 1
            temp_s -= 16
        else:
            t = 0
        rez[-i - 1] = hex10[temp_s]
    if t == 1 and len(a) == len(b):
        rez.appendleft('1')
    return ''.join(list(rez))


def multiplication(a, b, hex16, hex10):
    if len(a) < len(b):
        a, b = b, a
    rez = '0'
    k = 0
    for i in reversed(b):
        t = 0
        temp = ''
        for j in reversed(a):
            ai = hex16[j]
            bi = hex16[i]
            mi = ai * bi + t
            t1 = mi // 16
            mi = mi - t1 * 16
            t = t1
            temp = hex10[mi] + temp
        if t > 0:
            temp = hex10[t] + temp
        temp += "0" * k
        k += 1
        rez = summ(rez, temp, hex16, hex10)
    return rez


a = list(input('введите число А в шестнадцатиричной системе счисления: ').lower())
b = list(input('введите число B в шестнадцатиричной системе счисления: ').lower())

s = summ(a, b, hex16, hex10)
print(f'{"".join(a)} + {"".join(b)} = {s}')

m = multiplication(a, b, hex16, hex10)
print(f'{"".join(a)} * {"".join(b)} = {m}')
