"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

def yes_or_no(array):
    checked = []
    for item in array:
        if item not in checked:
            checked.append(item)
            print('No')
        else:
            print('Yes')

