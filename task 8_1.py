# 1.	Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.


import hashlib

substring_hash = set()
s = input('Введите строку: ')
l = len(s)
h_string = hashlib.sha1(s.encode('utf-8')).hexdigest()
for i in range(l + 1):
    for j in range(i, l + 1):
        if h_string != hashlib.sha1(s[i:j].encode('utf-8')).hexdigest() and len(s[i:j]) > 0:
            substring_hash.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(f'Количество различных подстрок в строке {s} - {len(substring_hash)}')
