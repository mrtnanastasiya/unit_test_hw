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

        numbers["name"] = get_name(doc_number)

        for doc_number in documents:
            self.assertEqual(doc_number,
                            '10006',
                            'Документ не найден')




