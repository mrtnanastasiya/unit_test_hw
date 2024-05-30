# Юнит-тест для ДЗ "Секретарь".

import unittest
from task3 import get_name, get_directory, add

class Task3TestCase(unittest.TestCase):

    def test_get_name(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
        ]

        directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

        result_name_1 = (get_name("10006"))
        self.assertEqual(result_name_1 ,
                            'Аристарх Павлов',
                            'Документ не найден')

        result_directory_1 = (get_directory("11-2"))
        self.assertEqual(result_directory_1,
                         '1',
                         'Полки с таким документом не найдено')

        result_name_2 = (get_name("101"))
        self.assertIn(result_name_2,
                         documents,
                         'Документ не найден')

        new_document = add('international passport', '311 020203', 'Александр Пушкин', 3)
        self.assertIn(new_document,
                         documents,
                         'Документ не найден')

        result_directory_2 = (get_directory("311 020203"))
        self.assertIn(result_directory_2,
                         documents,
                         'Полки с таким документом не найдено')

        result_name_3 = (get_name("311 020203"))
        self.assertIn(result_name_3,
                         documents,
                         'Документ не найден')

        result_directory_3 = (get_directory("311 020204"))
        self.assertIn(result_directory_3,
                      documents,
                      'Полки с таким документом не найдено')








