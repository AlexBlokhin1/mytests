#!/usr/bin/env
numbers_hundreds = {
    0: 'ноль',
    1: 'сто',
    2: 'двести',
    3: 'триста',
    4: 'четыреста',
    5: 'пятсот',
    6: 'шестсот',
    7: 'семсот',
    8: 'восемсот',
    9: 'девятсот'
}

numbers_dacades = {
    0:'',
    2: 'двадцать',
    3: 'тридцать',
    4: 'сорок',
    5: 'пятьдесят',
    6: 'шестьдесят',
    7: 'семьдесят',
    8: 'восемьдесят',
    9: 'девяносто'
}
numbers_figure = {
    0:'',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять'
}


def change_func(num):

    num = int(num)
    ddd = int(num // 100)           # 800
    dd = int(num % 100) // 10       # 20
    d = int(int(num % 100) % 10)    # 2

    print("{} {} {}".format(numbers_figure[ddd], numbers_figure[dd], numbers_figure[d]))


def change_func_REVERSE(num):
    xx = []
    for i in range(len(str(num))):
        dd = num % 10
        num = num // 10
        xx.append(numbers_figure[dd])
    xx.reverse()
    return xx


print(change_func_REVERSE(567))
print(change_func_REVERSE(516712385246))
print(change_func_REVERSE(35))
