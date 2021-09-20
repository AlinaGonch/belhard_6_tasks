"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n, fib=0, fib2=1):
    if n != 1:
        return fibonacci(n - 1, fib2, fib + fib2)
    else:
        return fib2
