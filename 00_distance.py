#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# Заполнение словаря
for city_1, coordinates_1 in sites.items():
    distances[city_1] = {}

    for city_2, coordinates_2 in sites.items():
        if city_1 != city_2:
            distance = (
                (coordinates_1[0] - coordinates_2[0]) ** 2
                + (coordinates_1[1] - coordinates_2[1]) ** 2
            ) ** 0.5

            distances[city_1][city_2] = round(distance, 2) # округление для красивого вывода

print(distances)
