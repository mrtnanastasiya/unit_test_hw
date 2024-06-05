
import unittest
import requests
import json
from code.ya import YaKlient

class YAClientTestCase(unittest.TestCase):

    def setUp(self):
       with open('secrets/ya_token.json', 'r') as file:
            data = json.load(file)
            token = data['token']
            self.ya_client = YaKlient(token)


    def test_create_folder(self):
        ok, status_code, error_text = self.ya_client.create_folder('disk:/NewFolder')

        # Получен код ошибки, при кот. мы не можем проверить создание папки.
        # Это может быть нехватка места на диске или тех. работы у яндекса.
        if status_code in [403, 409, 423, 503, 507]:
            self.skipTest(error_text)

        self.assertEqual(status_code,
                         201,
                         f'Папка не создана по причине: {error_text}')