def my_func(var_a, var_b, var_c):
    """
    Функция возвращает сумму двух наибольших чисел
    :param var_a: float; первое число
    :param var_b: float; второе число
    :param var_c: float; третье число
    :return: float; сумма двух наибольших аргументов из трех
    """
    var_list = [var_a, var_b, var_c]
    # Сортировка чисел по убыванию с помощью .sort()
    # var_list.sort(reverse=True)

    # Сортировка чисел по убыванию
    for i in range(1, len(var_list)):
        j = i
        # Меняем местами соседние элементы если последующий элемент больше предыдущего
        while j > 0 and var_list[j] > var_list[j-1]:
            var_list[j], var_list[j-1] = var_list[j-1], var_list[j]
            j -= 1

    return var_list[0] + var_list[1]


res_sum = my_func(float(input('Первое число:')),
                  float(input('Второе число:')),
                  float(input('Третье число:'))
                  )

print(f'Сумма двух наибольших чисел: {res_sum}')
