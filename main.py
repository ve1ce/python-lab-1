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


def main():
    print('--- Задание 00 ---')
    distances = calculate_distances()
    print(distances)

    print('\n--- Задание 01 ---')
    area, point_1_inside, point_2_inside = calculate_circle()
    print(area)
    print(point_1_inside)
    print(point_2_inside)

    print('\n--- Задание 02 ---')
    result = calculate_result()
    print(result)

    print('\n--- Задание 03 ---')
    movies = get_favorite_movies()
    print(movies[0])
    print(movies[1])
    print(movies[2])
    print(movies[3])

    print('\n--- Задание 04 ---')
    family, father_height, total_height = get_family_info()
    print('Рост отца -', father_height, 'см')
    print('Общий рост моей семьи -', total_height, 'см')

    print('\n--- Задание 05 ---')
    zoo, lion_cage, lark_cage = get_zoo()
    print(zoo)
    print('Лев находится в клетке', lion_cage)
    print('Жаворонок находится в клетке', lark_cage)

    print('\n--- Задание 06 ---')
    total_time, other_total_time = calculate_songs_time()
    print('Три песни звучат', total_time, 'минут')
    print('А другие три песни звучат', other_total_time, 'минут')

    print('\n--- Задание 07 ---')
    words = decode_message()
    print(' '.join(words))

    print('\n--- Задание 08 ---')
    all_flowers, common_flowers, only_garden, only_meadow = compare_flowers()
    print('Все виды цветов:', all_flowers)
    print('Растут и там, и там:', common_flowers)
    print('Только в саду:', only_garden)
    print('Только на лугу:', only_meadow)

    print('\n--- Задание 09 ---')
    sweets = get_sweets()
    print(sweets)

    print('\n--- Задание 10 ---')
    store_result = calculate_store()

    for product_name, product_info in store_result.items():
        print(
            product_name,
            '-',
            product_info['quantity'],
            'шт, стоимость',
            product_info['price'],
            'руб'
        )


if __name__ == '__main__':
    main()