# Словарь с русскими числительными
dict_num_rus = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
print(dict_num_rus)

with open('text_number_eng.txt', 'r', encoding='utf-8') as file_text_num_en, \
        open('text_number_rus.txt', 'w') as file_text_num_ru:
    # Считываем файл построчно
    for el in file_text_num_en.readlines():
        # Убираем символ окончания строки и образуем список из слова и числа
        # Берем слово и число
        num_text_en, value = el.split(' - ')
        # Определяем русское числительное и меняем строку
        var_str = el.replace(num_text_en, dict_num_rus.get(int(value)))
        file_text_num_ru.write(var_str)
        print(var_str)
