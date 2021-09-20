"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    fib = 0
    fib2 = 1
    if num_count == 0:
        raise ValueError('Введите значение больше 1')

    for i in range(num_count):
        fib, fib2 = fib2, fib + fib2
        yield fib


if __name__ == '__main__':
    fibonacci(5)
