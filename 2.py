# 2.1.3 - интерпретируемым языком
# 2.1.4 - все
# 2.1.5 - все
# 2.1.6 - создание графических GUI, создание приложений баз данных, создание приложений анализа данных,
# создание системных утилит, создание веб-приложений

# 2.2.2 - вывода данных на экран
# 2.2.3 - параметрами, аргументами
# 2.2.4
print("Здравствуй, мир!")
# 2.2.5
print(4, 8, 15, 16, 23, 42)
# 2.2.6
print(4)
print(8)
print(15)
print(16)
print(23)
print(42)
# 2.2.7
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')
# 2.2.9 - считывания данных с клавиатуры
# 2.2.10 - вывод текста "какой язык...", ввод данных, нажатие клавиши, запись в переменную, вывод текста
# 2.2.11
a = input()
print('Привет,', a)
# 2.2.12
a = input()
print(a, '- чемпион!')
# 2.2.13
a = input()
b = input()
c = input()
print(a)
print(b)
print(c)
# 2.2.14
a = input()
b = input()
c = input()
print(c)
print(b)
print(a)

# 2.3.2 - 31-12-2019
# 2.3.3 - Mercury*Venus!Mars**Jupiter?
# 2.3.4 - 5
# 2.3.5
print('I','like', 'Python', sep='***')
# 2.3.6
a = input()
b = input()
c = input()
d = input()
print(b, c, d, sep=a)
# 2.3.7
a = input()
print('Привет,', a, end='!')
# 2.3.9 - кроме 2teacher
# 2.3.10 - Pascal
# 2.3.11 - Python
# 2.3.13
print('Follow PEP8!')
print('Follow', 'PEP8!')
print('Follow', 'PEP8', sep='**')
name = input()
# 2.3.14 - Python+C#=awesome

# 2.4.2 - -50
# 2.4.3 - 20
# 2.4.4 - 4a
# 2.4.5
a = int(input())
b = a + 1
c = b + 1
print(a)
print(b)
print(c)
# 2.4.6
a, b, c = int(input()), int(input()), int(input())
print(a + b + c)
# 2.4.7
a = int(input())
print('Объем =', a*a*a)
print('Площадь полной поверхности =', 6*a*a)
# 2.4.8
a, b = int(input()), int(input())
f = 3*((a + b) * (a + b) * (a + b)) + 275*b*b - 127*a - 41
print(f)
# 2.4.9
num = int(input())
print('Следующее за числом', num, 'число:', num + 1)
print('Для числа', num, 'предыдущее число:', num - 1)
# 2.4.10
print((int(input()) + int(input()) + int(input()) + int(input())) * 3)
# 2.4.11
a, b = int(input()), int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
# 2.4.12
a1, d, n = int(input()), int(input()), int(input())
print(a1 + d*(n - 1))
# 2.4.13
a = int(input())
print(a, 2*a, 3*a, 4*a, 5*a, sep='---')

# 2.5.2 - 3, 4, 0, 12, -13
# 2.5.3 - 2, 0, 2, 3
# 2.5.4 - 29
# 2.5.5 - 2
# 2.5.6
b1, q, n = int(input()), int(input()), int(input())
print(b1*q**(n-1))
# 2.5.7
print( int(input()) // 100)
# 2.5.8
a, b = int(input()), int(input())
print(b // a)
print(b % a)
# 2.5.9
n = int(input())
print((n+1)//2)
# 2.5.10
a = int(input()) - 1
print(a // 4 + 1)
# 2.5.11
a = int(input())
print(a, 'мин - это', a // 60, 'час', a % 60, 'минут.')
# 2.5.13
a = int(input())
d1 = a // 100
d2 = (a // 10) % 10
d3 = a % 10
print('Сумма цифр =', d1 + d2 + d3)
print('Произведение цифр =', d1 * d2 * d3)
# 2.5.14
abc = int(input())
a = abc // 100
b = (abc // 10) % 10
c = abc % 10
print(a * 100 + b * 10 + c)
print(a * 100 + c * 10 + b)
print(b * 100 + a * 10 + c)
print(b * 100 + c * 10 + a)
print(c * 100 + a * 10 + b)
print(c * 100 + b * 10 + a)
# 2.5.15
d1, d2, d3, d4 = input()
print('Цифра в позиции тысяч равна', d1)
print('Цифра в позиции сотен равна', d2)
print('Цифра в позиции десятков равна', d3)
print('Цифра в позиции единиц равна', d4)
# 2.5.16
# a - n // 10000
# b - n % 10000 // 1000
# c - n % 1000 // 100
# d - n % 100 // 10
# e - n% 10