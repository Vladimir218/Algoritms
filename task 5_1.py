# 1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

qwentity = int(input('Введите количество предприятий: '))

factory = collections.Counter()
sum_profit = 0
for i in range(qwentity):
    factory_name, prifit = map(str, input(f'Предприятие {i + 1}. Введите название и прибыли: ').split())
    sum_profit += float(prifit)
    factory[factory_name] = float(prifit)
avg_profit = sum_profit / qwentity

print('Наименования предприятий с прибылью выше средней: ')
for i in factory:
    if factory[i] > avg_profit:
        print(i, end="\n")
print('Наименования предприятий с прибылью ниже средней: ')
for i in factory:
    if factory[i] < avg_profit:
        print(i, end="\n")
