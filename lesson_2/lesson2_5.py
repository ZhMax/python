# Существующий список из натуральных чисел
var_list = [7, 6, 5, 5, 3, 3, 2]

# Вводим новое число
new_num = int(input('Введите натуральное число:'))

# Добавляем число в список
var_list.append(new_num)

# Сортируем список
var_list.sort(reverse=True)

# Выводим результат
print(var_list)
