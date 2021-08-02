from itertools import count, cycle
from sys import argv


def gen_int(num_start):

    """
    Генератор последовательности чисел

    :param num_start: первый элемент последовательности
    :yield: текущий элемент последовательности
    """

    for el in count(num_start):
        # Выход из цикла при достижении максимального количества
        # выведенных чисел
        if el > num_start+10:
            break
        yield(el)


# Передача данных в программу
num_int_script, num_initial_param = argv

# Вывод последовательности чисел
for el in gen_int(int(num_initial_param)):
    print(el)

var_list = ['a', 'b', 'c', '1']
# Счетчик выведенных символов
var_limit = 0
for el in cycle(var_list):
    # Выход из цикла при достижении максимального количества
    # выведенных символов
    if var_limit > 25:
        break
    else:
        var_limit += 1
        print(el)
