from functools import reduce

# Открываем файл и считываем данные
with open('text_lessons.txt', 'r', encoding='utf-8') as file_text_in:
    list_all_data = file_text_in.readlines()
    print('Прочитанные данные:')
    print(list_all_data)

# Определяем список с названиями дисциплин
list_lessons = [el.split(':')[0] for el in list_all_data]
# Определяем список из строк с количеством занятий. Убираем лишние пробелы
list_data = [el.split(':')[1].strip(' ') for el in list_all_data]
# В каждой строке находим числа с количеством занятий
# Создаем список из списков чисел для каждой дисциплины
list_num_subj = []
for el_str in list_data:
    i = 0
    # Список из чисел с количеством занятий для каждой дисциплины
    var_list = []
    # Находим числа в строке el_str
    while i < len(el_str):
        #  Если символ i является цифрой, то смотрим соседние символы,
        # чтобы составить число
        if el_str[i].isdigit():
            j = i
            while el_str[j].isdigit():
                j += 1
            # Добавляем найденное число в строку
            var_list.append(int(el_str[i:j]))
            i = j

        i += 1
    # Добавляем список с числами к общему списку для всех дисциплин
    list_num_subj.append(var_list)

# Функция суммы двух чисел
func_sum = lambda x, y: x + y

# Список с общим количеством занятий по каждой дисциплине
res_sum_num_subj = [reduce(func_sum, el) for el in list_num_subj]

# Словарь с названием дисциплины и количеством занятий
res_dict_lessons_num_subj = dict(zip(list_lessons, res_sum_num_subj))
print('Словарь с названием дисциплины и количеством занятий:')
print(res_dict_lessons_num_subj)
