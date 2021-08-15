class Data:
    # Динамический атрибут для даты
    def __init__(self, str_data):
        self.str_data = str_data
    # Метод класса для получения числа дня, месяца и года
    @classmethod
    def data_to_number(cls, str_var):
        res_list = [int(el) for el in str_var.split('-') if el.isdigit()]
        return res_list if len(res_list) == 3 else 'Дата введена некорректно!'

    # Метод класса для проверки введенных данных
    @staticmethod
    def data_validation(str_var):
        var_day, var_month, var_year = Data.data_to_number(str_var)
        # Проверка года
        if var_year > 0:
            # Проверка месяца
            if 1 <= var_month <= 12:
                # Проверяем количество дней в месяце, исходя из того что он принадлежит первому полугодию
                if var_month in range(1, 8) and var_month % 2 == 0:
                    # Если месяц февраль, то проверяем является ли год високосным
                    if var_month == 2:
                        if var_year in range(4, var_year+1, 4):
                            if 1 <= var_day <= 29:
                                return 'Дата введена верно!'
                            else:
                                return 'День введен неверно!'
                        else:
                            if 1 <= var_day <= 28:
                                return 'Дата введена верно!'
                            else:
                                return 'День введен неверно!'
                    else:
                        if 1 <= var_day <= 30:
                            return 'Дата введена верно!'
                        else:
                            return 'День введен неверно!'
                if var_month in range(1, 8) and var_month % 2 == 1:
                    if 1 <= var_day <= 31:
                        return 'Дата введена верно!'
                    else:
                        return 'День введен неверно!'
                # Проверяем количество дней в месяце, исходя из того что он принадлежит второму полугодию
                if var_month in range(8, 12) and var_month % 2 == 0:
                    if 1 <= var_day <= 31:
                        return 'Дата введена верно!'
                    else:
                        return 'День введен неверно!'
                if var_month in range(8, 12) and var_month % 2 == 1:
                    if 1 <= var_day <= 30:
                        return 'Дата введена верно!'
                    else:
                        return 'День введен неверно!'
            else:
                return 'Месяц введен неверно!'
        else:
            return 'Год введен неверно!'


print(Data.data_to_number('10-вцй-1993'))

print(Data.data_to_number('10-06-1993'))
print(Data.data_validation('10-06-1993'))

print(Data.data_to_number('332-03-1950'))
print(Data.data_validation('332-03-1950'))

print(Data.data_to_number('12-55-2174'))
print(Data.data_validation('12-55-2174'))


print(Data.data_to_number('31-07-2000'))
print(Data.data_validation('31-07-2000'))

print(Data.data_to_number('31-08-2010'))
print(Data.data_validation('31-08-2010'))

print(Data.data_to_number('31-09-2010'))
print(Data.data_validation('31-09-2010'))

print(Data.data_to_number('29-02-2019'))
print(Data.data_validation('29-02-2019'))

print(Data.data_to_number('28-02-2019'))
print(Data.data_validation('28-02-2019'))

print(Data.data_to_number('29-02-2020'))
print(Data.data_validation('29-02-2020'))


