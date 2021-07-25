def func_rel(var_num, var_denom):
    """
    Функция находит частное от деления двух чисел
    :param var_num: float; числитель
    :param var_denom: float; знаменатель
    :return: float; возвращает результат деления либо предупреждение
    """
    if var_denom != 0:
        return var_num/var_denom
    else:
        return 'Деление на ноль!'

# Запрос входных данных
x = float(input('Введите числитель:'))
y = float(input('Введите знаменатель:'))

# Вывод результата
print(f'Частное: {func_rel(x, y)}')
