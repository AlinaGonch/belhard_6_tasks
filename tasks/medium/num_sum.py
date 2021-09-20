"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n, summa=0):
    if len(str(n)) == 0:  # return sum([int(el) for el in str(n)])
        return summa
    else:
        return sum_of_numbers(str(n)[1:], summa + int(str(n)[0]))
