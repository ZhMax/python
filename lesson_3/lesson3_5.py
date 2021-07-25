def sum_func():
    """
    Функция содержит текущую сумму введенных чисех var_sum и функцию el_func,
    которая увеличивает сумму var_sum на одно прочитанное число var_el
    :return: None
    """
    var_sum = 0

    def el_func(var_el):
        """
        Функция добавляет к текущей сумме введенных чисел var_sum прочитанное число var_el
        :param var_el: float; прочитанное число
        :return: var_sum: float; текущая сумма введенных чисел
        """
        nonlocal var_sum
        var_sum += var_el
        return var_sum

    return el_func


print('Программа вычисляет сумму введенных чисел.')
print('Если в строке будет обнаружен специальный символ @, то расчет прекратится.')

# Вызов функции добавления прочитанного в строке числа к текущей сумме
func_el = sum_func()
i = 0

while i == 0:
    j = 0
    var_str = input('Введите строку из чисел, разделенных пробелами:')
    # Убираем лишние пробелы
    while var_str.find('  ') > -1:
        var_str = var_str.replace('  ', ' ')

    # Разбиваем строку на числа по разделителю
    var_list = var_str.split(' ')

    # Подсчитаем сумму чисел в введенной строке
    for el in var_list:
        if el.isdigit():
            func_el(float(el))
        elif el == '@':
            print('В строке был обнаружен специальный символ!')
            j = 1
            i = 1
            break
        else:
            print('В строке присутствуют нечисловые типы данных!')
            j = 1
            i = 1
            break
    # Вывод результата
    print(f'Сумма введенных чисел: {func_el(0)}')

    # Запрос на продолжение ввода
    while j == 0:
        print('Продолжить ввод строки чисел?')
        var_answ_next = input('да/нет:').lower()
        if var_answ_next == 'да':
            j = 1
        elif var_answ_next == 'нет':
            i = 1
            j = 1