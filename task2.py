print('Введите трехзначное число: ')
a = int(input())
n = 0

'''Changes in file'''
while a > 0:
    n += a % 10
    a //= 10
print('Сумма цифр', n)