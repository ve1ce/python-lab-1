#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
def get_family_info():
    # моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
    my_family = ['Я', 'Отец', 'Мать']

    # список списков приблизительного роста членов вашей семьи
    my_family_height = [
        ['Я', 170],
        ['Отец', 175],
        ['Мать', 166],
    ]

    # Выведите на консоль рост отца в формате
    #   Рост отца - ХХ см

    # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
    #   Общий рост моей семьи - ХХ см

    father_height = my_family_height[1][1]

    total_height = 0

    for person in my_family_height:
        total_height += person[1]

    return my_family, father_height, total_height

if __name__ == '__main__':
    family, father_height, total_height = get_family_info()

    print('Рост отца -', father_height, 'см')
    print('Общий рост моей семьи -', total_height, 'см')