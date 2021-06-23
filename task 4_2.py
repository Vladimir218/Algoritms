# Урок 4. Задание 2.	Написать два алгоритма нахождения i-го по счёту простого числа.
# ●	Без использования Решета Эратосфена;
# ●	Использовать алгоритм решето Эратосфена

import cProfile
# _________Алгоритм вычисления простого числа _________
def is_prime(n):
    m = int(n ** 1 / 2)
    log_prime = True
    if m > 1:
        for i in range(2, int(n ** 1 / 2)+1):
            if n % i == 0:
                log_prime = False
                break
    return log_prime


def prime_number(i):
    count = 0
    prime = 2
    nm = 3
    i -=1
    if i > 0:
        while count < i:
            if is_prime(nm):
                count += 1
                prime = nm
            nm += 1
    return prime


i = int(input('Введите i: '))
print(f'{i} простое число {prime_number(i)}')
print(cProfile.run("prime_number(i)"))
# __________ Алгоритм вычисления простого числа используя решето Эратосфена _______________
def i_prime(i,numbers):
    prime_count = 0
    while i > prime_count and numbers:
        num = min(numbers)
        prime_count +=1
        numbers -= set(range(num,2*10**6+1,num))
    return num


numbers = set(range(2,2*10**6+1))
i = int(input('Введите i: '))
prime = i_prime(i,numbers)
print (f'{i}-е простое число равно {prime}')
print(cProfile.run("i_prime(i,numbers)"))

# Скорость алгоритмов оценим с помощью cProfile (по результатам измерений первый алгоритм существенно быстрее)
# 1- алг
# 543 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 task 4_2.py:18(prime_number)
#       539    0.003    0.000    0.003    0.000 task 4_2.py:7(is_prime)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# None
#
# 2 - алг
# 104 function calls in 2.558 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.558    2.558 <string>:1(<module>)
#         1    0.091    0.091    2.558    2.558 task 4_2.py:36(i_prime)
#         1    0.000    0.000    2.558    2.558 {built-in method builtins.exec}
#       100    2.467    0.025    2.467    0.025 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# None
#
# Сложность 1-го алгоритма - O(n**3/2)
# Сложность 2-го алгоритма - O(n*log n)