# Юнит-тест для ДЗ "Секретарь".

import unittest
from task3 import get_name, get_directory, add, documents, directories


class Task3TestCase(unittest.TestCase):

    def setUp(self):
        add('passport', '2207 876234', 'Василий Гупкин', 1)
        add('invoice', '11-2', 'Геннадий Покемонов', 1)
        add('driver license', '5455 028765', 'Василий Иванов', 1)
        add('insurance', '10006', 'Аристарх Павлов', 2)

    def test_get_name(self):

        result_name_1 = get_name("10006")
        self.assertEqual(result_name_1,
                              'Аристарх Павлов',
                              'Документ не найден')

        result_name_2 = get_name("101")
        self.assertIsNotNone(result_name_2,
                          'Документ не найден')

        result_name_3 = get_name("311 020203")
        self.assertIsNotNone(result_name_3,
                          'Документ не найден')

        result_name_4 = get_name("311 020203")
        self.assertEqual(result_name_4,
                         'Александр Пушкин',
                         'Документ не найден')

    def test_get_directory(self):

        result_directory_1 = get_directory("11-2")
        self.assertEqual(result_directory_1,
                         '1',
                         'Полки с таким документом не найдено')

        result_directory_2 = get_directory("311 020203")
        self.assertIsNone(result_directory_2,
                         'Полки с таким документом не найдено')

        result_directory_3 = get_directory("311 020204")
        self.assertIsNone(result_directory_3,
                          'Полки с таким документом не найдено')

    def test_add(self):
        new_document = add('international passport', '311 020203', 'Александр Пушкин', 3)







