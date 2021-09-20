"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(data: dict, grade):
    data[grade] += 1


def decr_students(data: dict, grade):
    if data[grade] > 0:
        data[grade] -= 1


def add_class(data: dict, grade):
    data.setdefault(grade, 0)


def remove_class(data: dict, grade):
    del data[grade]


def calc_students(data: dict):
    summa = 0
    for value in data.values():
        summa += value
    return summa


if __name__ == '__main__':
    incr_students(school_data, '1a')
    print(school_data)
