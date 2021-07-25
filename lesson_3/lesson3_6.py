def int_func(var_el):
    """
    Функция возвращает строку с заглавной буквы
    :var_el: str; Принимаемая строка
    :return: str; Строка с заглавной буквы
    """
    # Очевидное решение
    # return var_el.capitalize()

    # Список из букв
    var_list = list(var_el)
    # Решение посредством получения ASCII кода символа
    if ord('a') <= ord(var_el[0]) <= ord('z'):
        # Английский алфавит
        var_list[0] = chr(ord(var_el[0]) + ord('A') - ord('a'))
    elif ord('а') <= ord(var_el[0]) <= ord('я'):
        # Русский алфавит
        var_list[0] = chr(ord(var_el[0]) + ord('А') - ord('а'))

    return ''.join(var_list)



var_str = input('Введите строку из слов в нижнем регистре, разделенных пробелами:').lower()
# Убираем лишние пробелы
while var_str.find('  ') > -1:
    var_str = var_str.replace('  ', ' ')


# Разбиваем строку на числа по разделителю
var_list = var_str.split(' ')
var_res = []
for el in var_list:
    if el[0].isalpha():
        var_res.append(int_func(el))
    else:
        print(f'Первый символ {el} не является буквой!')

print('Строка из слов с заглавными буквами:')
print(' '.join(var_res))