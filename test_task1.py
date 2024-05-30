# Юнит-тест для ДЗ "сисадмин".

import unittest
from task1 import solve

class Task1TestCase(unittest.TestCase):
    def test_solve(self):
        models = ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
                  '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
                  '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
                  '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500']
        available = [1, 1, 1, 1, 0, 1, 1, 0]
        manufacturers = ['Intel', 'Samsung', 'WD']

        # ssds - список дисков, кот. купит сисадмин,
        # count - сколько компьютеров он починит
        ssds, count = solve(models, available, manufacturers)

        # self.assertIn(a,b) - проверяет, что элемент a находится в коллекции (здесь список) b
        # Проверяем, что все нужные диски присутсвуют в списке покупок
        for disk_name in ['480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO']:
            self.assertIn(disk_name,
                            ssds,
                            f'{disk_name} не присутствует в "списке покупок"')


        # Проверяем по длине списка покупок, что нет лишних элементов
        self.assertEqual(count,
                         2,
                         'Неверное кол-во компьютеров')

        # Здесь мы проверили правильность списка покупок от сисадмина
        # Проверка на равенство списков чувствительна к порядку элементов
        # поэтому self.Equal не самое идеальное решение
        # поэтому мы сначала проверили, что нужные диски входят в список покупок,
        # а затем проверили кол-во дисков в списке покупок, чтобы
        # убедиться, что в списке нет лишних дисков!!
