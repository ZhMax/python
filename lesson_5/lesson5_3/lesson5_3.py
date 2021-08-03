# Открытие файла с помощью менеджера контекста
with open('text_salary.txt', 'r', encoding='utf-8') as file_obj_text:
    # Считываем файл построчно
    var_list = file_obj_text.readlines()
    # Образуем словарь
    var_dict = dict([tuple(el.split()) for el in var_list])

    # Определяем имена сотрудников, получающих меньше 20 тыс.
    print('Сотрудники, получающие меньше 20 тыс.:')
    var_list_salary = []
    for key, value in var_dict.items():
        if float(value) < 20000:
            var_list_salary.append(float(value))
            print(key)

    # Подсчитываем средннюю зарпалату данных сотрудников
    var_sum_salary = 0
    # Вычисляем сумму зарплат
    for el in var_list_salary:
        var_sum_salary += el
    # Определяем среднее
    res_mean_salary = var_sum_salary / len(var_list_salary)
    print(f'Средняя зарпалата данных сотрудников: {res_mean_salary:.1f}')
