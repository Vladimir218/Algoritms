# 4.	Определить, какое число в массиве встречается чаще всего.


from random import randrange
dic = {}
x,y = map(int, input('Введите диапазон (x,y) формирования массива чисел: ').split())

a = [0]*(y-x+1)
for i in range(y-x+1):
    a[i] = randrange(x,y)
print(a)
for i in a:
    if dic.get(i):
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
print(f'В массиве чаще встречается число {max(dic, key=dic.get)}')