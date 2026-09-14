#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compare_flowers():
    # В саду сорвали цветы
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

    # На лугу сорвали цветы
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

    # Создайте множество цветов, произрастающих в саду и на лугу
    # garden_set =
    # meadow_set =
    garden_set = set(garden)
    meadow_set = set(meadow)

    # Выведите на консоль все виды цветов
    all_flowers = garden_set | meadow_set

    # Выведите на консоль те, которые растут и там и там
    common_flowers = garden_set & meadow_set

    # Выведите на консоль те, которые растут в саду, но не растут на лугу
    only_garden = garden_set - meadow_set

    # Выведите на консоль те, которые растут на лугу, но не растут в саду
    only_meadow = meadow_set - garden_set

    return all_flowers, common_flowers, only_garden, only_meadow

if __name__ == '__main__':
    all_flowers, common_flowers, only_garden, only_meadow = compare_flowers()

    print('Все виды цветов:', all_flowers)
    print('Растут и там, и там:', common_flowers)
    print('Только в саду:', only_garden)
    print('Только на лугу:', only_meadow)