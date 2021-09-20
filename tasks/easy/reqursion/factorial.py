"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n, fac=1):
    if n != 1:
        fac *= n
        return factorial(n - 1, fac)
    else:
        return fac
