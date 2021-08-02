# Запрашиваем элементы списка
var_input_str = input('Введите список чисел через пробел:')

# Убираем лишние пробелы
while var_input_str.find('  ') > -1:
    var_str = var_input_str.replace('  ', ' ')

# Разбиваем строку на числа по разделителю
var_input_list = var_input_str.split(' ')
num_list = []

for el in var_input_list:
    try:
        num_list.append(float(el))
    except ValueError:
        print(f'Элемент {el} не является числом')

# Проверка условия того, что текущий элемент больше предыдущего
out_list = [num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i-1]]

# Вывод результата
print('Отсортированный список:')
print(out_list)

