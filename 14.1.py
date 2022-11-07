# 14.1.1 - 2
# 14.1.2 - i, res, n
# 14.1.3 - локальной, функции, значение, переменная, локальной
# 14.1.4
def draw_triangle():
    n = 15
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)

draw_triangle()

# 14.1.5
def get_shipping_cost(quantity):
    return 1000 + 120 * (quantity - 1)

n = int(input())

print(get_shipping_cost(n))

# 14.1.6
def compute_binom(n, k):
    from math import factorial
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

n = int(input())
k = int(input())

print(compute_binom(n, k))

# 14.1.7
def number_to_words(num):
    s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто','']
    if num <= 20:
        return s[num - 1]
    else:
        return s[num // 10 - 1 + 18] + ' ' + s[num % 10 - 1]

n = int(input())

print(number_to_words(n))

# 14.1.8
def get_month(language, number):
    monthsRu = { 1 : 'январь', 2 : 'февраль', 3 : 'март', 4 : 'апрель', 5 : 'май', 6 : 'июнь', 7 : 'июль', 8 : 'август', 9 : 'сентябрь', 10 : 'октябрь', 11 : 'ноябрь', 12 : 'декабрь'}
    monthsEn = { 1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august', 9 : 'september', 10 : 'october', 11 : 'november', 12 : 'december'}
    if language == 'ru':
        return monthsRu[number]
    else:
        return monthsEn[number]

lan = input()
num = int(input())

print(get_month(lan, num))

# 14.1.9
def is_magic(date):
    day, month, year = date.split('.')
    return int(day) * int(month) == int(year) % 100

date = input()

print(is_magic(date))

# 14.1.10
def is_pangram(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in text.lower():
        if letter in letters:
            letters.remove(letter)
    return len(letters) == 0

text = input()

print(is_pangram(text))