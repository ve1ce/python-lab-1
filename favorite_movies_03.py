#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов
def get_favorite_movies():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    # Выведите на консоль с помощью индексации строки, последовательно:
    #   первый фильм
    #   последний
    #   второй
    #   второй с конца

    # Запятая не должна выводиться. Переопределять my_favorite_movies нельзя.
    # Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
    # как указано в задании!

    first_movie = my_favorite_movies[:10]

    last_movie = my_favorite_movies[-15:]

    second_movie = my_favorite_movies[12:25]

    second_from_end = my_favorite_movies[-22:-17]

    return first_movie, last_movie, second_movie, second_from_end

if __name__ == '__main__':
    movies = get_favorite_movies()

    print(movies[0])
    print(movies[1])
    print(movies[2])
