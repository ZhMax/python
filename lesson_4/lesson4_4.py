# Запрашиваем элементы списка
var_input_str = input('Введите список чисел через пробел:')

# Убираем лишние пробелы
while var_input_str.find('  ') > -1:
    var_input_str = var_input_str.replace('  ', ' ')

# Разбиваем строку на числа по разделителю
var_input_list = var_input_str.split(' ')
num_list = []

for el in var_input_list:
    try:
        num_list.append(float(el))
    except ValueError:
        print(f'Элемент {el} не является числом')

# Формируем список из уникальных чисел
out_list = [el for el in num_list if num_list.count(el) == 1]

print('Уникальные элементы введенного списка:')
print(out_list)
