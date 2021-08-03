from random import randint

# Количество случайных чисел
num_size = 3

# Записываем последовательность случайных чисел в файл
with open('text_number_list.txt', 'w') as file_num_out:
    # Генерируем последовательность строк из случайных чисел
    var_list = [str(randint(-100, 100)) for i in range(0, num_size)]
    # Записываем последовательность в файл
    print(' '.join(var_list), file=file_num_out)
    print('Сгенерированная последовательность: ', ' '.join(var_list))

# Считываем последовательность чисел из файла и вычисляем их сумму
res_sum = 0
with open('text_number_list.txt', 'r') as file_num_in:
    # Считываем строку из чисел
    var_str = file_num_in.read()
    # Разделяем строку по пробелам
    var_list = var_str.split()
    # Подсчитываем сумму чисел
    for el in var_list:
        res_sum += int(el)
    print(f'Сумма чисел: {res_sum}')
