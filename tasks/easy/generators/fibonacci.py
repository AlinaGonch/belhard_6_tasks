"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""
def fibonacci():
    fib = 0
    fib2 = 1
    while True:
        fib, fib2 = fib2, fib + fib2
        yield fib
