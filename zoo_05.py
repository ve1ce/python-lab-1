#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
def get_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

    # Посадите медведя (bear) между львом и кенгуру
    # и выведите список на консоль

    zoo.insert(1, 'bear')


    # Добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark']
    # и выведите список на консоль
    zoo.extend(birds)


    # Уберите слона (elephant) из зоопарка
    # и выведите список на консоль
    zoo.remove('elephant')

    lion_cage = zoo.index('lion') + 1
    lark_cage = zoo.index('lark') + 1

    return zoo, lion_cage, lark_cage


# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
if __name__ == '__main__':
    zoo, lion_cage, lark_cage = get_zoo()

    print(zoo)
    print('Лев находится в клетке', lion_cage)
    print('Жаворонок находится в клетке', lark_cage)
