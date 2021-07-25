def func_user_data(var_name, var_surname, var_birthdate,
                   var_city, var_email, var_tel):
    """
    Функция возвращает строку введенных данных о пользователе
    :param var_name: str; Имя
    :param var_surname: str; Фамилия
    :param var_birthdate: str; Дата рождения
    :param var_city: str; Город
    :param var_email: str; E-mail
    :param var_tel: str; Телефон
    :return: str; строка данных о пользователе
    """
    return ' '.join([var_name, var_surname, var_birthdate,
                     var_city, var_email, var_tel])


# Запрос данных
print('Введите данные пользователя:')
res_str = func_user_data(var_name=input('Имя:'),
                         var_surname=input('Фамилия:'),
                         var_birthdate=input('Дата рождения:'),
                         var_city=input('Город:'),
                         var_email=input('E-mail:'),
                         var_tel=input('Телефон:'))

# Вывод результата
print('Данные пользователя:')
print(res_str)
