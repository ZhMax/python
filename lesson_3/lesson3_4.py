def my_func(var_num, var_deg):
    """
    Функция возводит число var_num в степень var_deg
    :param var_num: float; действительное число,
                           которое возводится в степень
    :param var_deg: int; целочисленный показатель степени
    :return: float; результат возведения числа var_num в степень var_deg
    """
    var_res = 1
    # Возводим число var_num в положительную степень abs(var_deg)
    for i in range(0, abs(var_deg)):
        var_res = var_res * var_num
    # Выполняем деление если степень отрицательная
    if var_deg < 0:
        var_res = 1 / var_res
    return var_res


# Запрос данных
x = float(input('Введите действительное положительное число x:'))
alpha = int(input('Введите целое число alpha:'))

# Проверка условия положительности числа x
if x > 0:
    res_pow = my_func(x, alpha)
    print(f'x^alpha = {res_pow}')
else:
    print('x - неположительное число')
