import pytest

from distance_00 import calculate_distances
from circle_01 import calculate_circle
from operations_02 import calculate_result
from favorite_movies_03 import get_favorite_movies
from my_family_04 import get_family_info
from zoo_05 import get_zoo
from songs_list_06 import calculate_songs_time
from secret_07 import decode_message
from garden_08 import compare_flowers
from shopping_09 import get_sweets
from store_10 import calculate_store


def test_distance():
    distances = calculate_distances()

    assert distances['Moscow']['London'] == pytest.approx(145.60219778561037)
    assert distances['Moscow']['Paris'] == pytest.approx(130.38404810405297)
    assert distances['London']['Paris'] == pytest.approx(42.42640687119285)


def test_circle():
    area, point_1_inside, point_2_inside = calculate_circle()

    assert area == 5541.7693
    assert point_1_inside is True
    assert point_2_inside is False


def test_operations():
    assert calculate_result() == 25


def test_favorite_movies():
    movies = get_favorite_movies()

    assert movies == (
        'Терминатор',
        'Назад в будущее',
        'Пятый элемент',
        'Чужие',
    )


def test_my_family():
    family, father_height, total_height = get_family_info()

    assert family == ['Я', 'Отец', 'Мать']
    assert father_height == 175
    assert total_height == 511


def test_zoo():
    zoo, lion_cage, lark_cage = get_zoo()

    assert zoo == [
        'lion',
        'bear',
        'kangaroo',
        'monkey',
        'rooster',
        'ostrich',
        'lark',
    ]

    assert lion_cage == 1
    assert lark_cage == 7


def test_songs():
    total_time, other_total_time = calculate_songs_time()

    assert total_time == 14.93
    assert other_total_time == 13.49


def test_secret():
    words = decode_message()

    assert words == (
        'в',
        'бане',
        'веник',
        'дороже',
        'денег',
    )


def test_garden():
    all_flowers, common_flowers, only_garden, only_meadow = compare_flowers()

    assert all_flowers == {
        'ромашка',
        'роза',
        'одуванчик',
        'гладиолус',
        'подсолнух',
        'клевер',
        'мак',
    }

    assert common_flowers == {
        'ромашка',
        'одуванчик',
    }

    assert only_garden == {
        'роза',
        'гладиолус',
        'подсолнух',
    }

    assert only_meadow == {
        'клевер',
        'мак',
    }


def test_shopping():
    sweets = get_sweets()

    assert sweets == {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
        'конфеты': [
            {'shop': 'магнит', 'price': 30.99},
            {'shop': 'пятерочка', 'price': 32.99},
        ],
        'карамель': [
            {'shop': 'магнит', 'price': 41.99},
            {'shop': 'ашан', 'price': 45.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ],
    }


def test_store():
    result = calculate_store()

    assert result == {
        'Лампа': {
            'quantity': 27,
            'price': 1134,
        },
        'Стол': {
            'quantity': 54,
            'price': 27860,
        },
        'Диван': {
            'quantity': 3,
            'price': 3550,
        },
        'Стул': {
            'quantity': 105,
            'price': 10311,
        },
    }