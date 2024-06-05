# Юнит-тест для ДЗ "кулинарная книга".

import unittest
from code.task2 import solve

class Task2TestCase(unittest.TestCase):
    def test_solve(self):

        my_cook_book = [
            ['Шарлотка',
             [
                 ['мука', 1, 'ст.'],
                 ['сахар', 1, 'ст.'],
                 ['яйца', 3, 'шт.'],
                 ['яблоки', 4, 'шт.'],
                 ['ванилин', 1, 'щеп.'],
             ]
             ],
            ['Сырники',
             [
                 ['творог', 400, 'гр.'],
                 ['яйца', 2, 'шт.'],
                 ['сахар', 4, 'ст.л.'],
                 ['мука', 3, 'ст.л.'],
                 ['масло растительное', 1, 'ст.л.'],
             ],
             ]
        ]

        person = 3
        answer = ['Шарлотка: мука 3 ст., сахар 3 ст., яйца 9 шт., яблоки 12 шт., ванилин 3 щеп.',
                  'Сырники: творог 1200 гр., яйца 6 шт., сахар 12 ст.л., мука 9 ст.л., масло растительное 3 ст.л.']


        result = solve(my_cook_book, person)
        # print(result)
        # print(answer)

        for dish in answer:
            self.assertIn(dish,
                          result,
                          f'{dish} не присутствует в "кулинарной книге"')

        self.assertEqual(len(result),
                         len(answer),
                         'В списке есть лишние элементы, либо их недостаточно')




