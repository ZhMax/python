class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Вводите строки числе через пробел. Для окончания программы введите "stop".')
# Параметр завершения ввода
out_index = 0
# Результирующий список из чисел
res_list = []
while out_index == 0:
    # Запрос данных
    str_input = input('Введите строку из чисел через пробел: ')
    for el in str_input.split():
        # Проверка кодового слова
        if el != 'stop':
            try:
                # Проверка, является ли строка el целым числом
                if el.isdigit():
                    res_list.append(int(el))
                # Проверка, является ли строка el десятичной дробью
                elif el.count('.') == 1:
                    if el.split('.')[0].isdigit() and el.split('.')[1].isdigit():
                        res_list.append(float(el))
                # Вызов ошибки если el не является числом
                else:
                    raise NumError(f'Элемент {el} не является числом')
            except NumError as err:
                print(err)
        else:
            out_index = 1
            print('Ввод завершен!')
    print(f'Список из чисел: {res_list}')

