'''
9.	Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
def summ(n):
    s=0;
    n= int(n);
    while n > 0:
        s += n % 10;
        n = n // 10;
    return s;

n='';
maxsum=0;
maxdidgit =''
while n.lower() != 'q':
    n = input('Введите число (для завершения ввода нажмите q): ');
    if n.isdigit():
        s = summ(n)
        if maxsum < s:
            maxsum = s;
            maxdidgit =n;

print(f'Число {maxdidgit} имеет максимальную сумму цифр');

