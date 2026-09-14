#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
def calculate_distances():
    сites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    # Составим словарь словарей расстояний между ними
    # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    distances = {}

    # Заполнение словаря
    for city_1, coordinates_1 in сites.items():
        distances[city_1] = {}

        for city_2, coordinates_2 in сites.items():
            if city_1 != city_2:
                distance = (
                    (coordinates_1[0] - coordinates_2[0]) ** 2
                    + (coordinates_1[1] - coordinates_2[1]) ** 2
                ) ** 0.5

                distances[city_1][city_2] = distance

    return distances

if __name__ == '__main__':
    print(calculate_distances())
