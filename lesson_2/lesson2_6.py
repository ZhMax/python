# Формируем структуру
# Список товаров с характеристиками
prod_list = []

# Заполняем форму
i = 0
product_num = 0
while i == 0:
    # Номер товара
    product_num += 1

    # Характеристики товара
    print('Введите параметры товара')
    # par_name = input('название:')
    par_name = ('название', input('название:'))
    par_price = ('цена', float(input('цена:')))
    par_num = ('количество', int(input('количество:')))
    par_unit = ('единица измерения', input('единица измерения:'))

    # Список характеристик товара
    prod_list.append((product_num, dict([par_name, par_price, par_num, par_unit])))

    print('Ввести данные для следующего товара?')
    j = 0
    while j == 0:
        var_answ_next = input('да/нет:').lower()
        if var_answ_next == 'да':
            j = 1
        elif var_answ_next == 'нет':
            i = 1
            j = 1

print("Введенная структура:")
print(prod_list)
# prod_list = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]

# Список для анализа данных
prod_analysis_list = []

# Список ключей, по которым выполняется анализ
prod_list_keys = list(prod_list[0][1].keys())
var_tuple = (prod_list_keys[0], [])

# Цикл по всем ключам
for i in range(0, len(prod_list_keys)):
    # Переменная, которая хранит кортеж (i ключ, его значение)
    var_tuple = (prod_list_keys[i], [])
    # Цикл по всем товарам
    for j in range(0, len(prod_list)):
        # Добавляем значение товара j, которое соответствует ключу i
        var_tuple[1].append(prod_list[j][1].get(prod_list_keys[i]))
    # Добавляем, полученный кортеж с ключем и его возможными значениями
    # к списку для аналитики
    prod_analysis_list.append(var_tuple)

# Словарь для анализа данных из полученного списка
prod_analysis_dict = dict(prod_analysis_list)

print("Словарь для аналитики данных:")
print(prod_analysis_dict)

