"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generate_brackets(length, string='', opened=0, closed=0):
    if opened == length and closed == length:
        print(string)
    else:
        if opened < length:
            generate_brackets(length, string + '(', opened + 1, closed)
        if closed < opened:
            generate_brackets(length, string + ')', opened, closed + 1)
