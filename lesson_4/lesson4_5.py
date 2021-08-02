from functools import reduce


def func_prod(prev_prod, el):
    """
    Функция выполняет произведение двух чисел

    :param prev_prod: float; первый множитель
    :param el: float; второй множитель
    :return: float; результат умножения

    """
    return prev_prod * el


# Список четных чисел от 100 до 1000
num_list = [el for el in range(100, 1001, 2)]
# Произведение всех чисел списка num_list
res_prod = reduce(func_prod, num_list)

print('Произведение всех четных чисел от 100 до 1000 равно:')
print(res_prod)

