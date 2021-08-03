# Открываем файл
file_obj_text = open('text_math.txt', 'r', encoding='utf-8')

# Считываем файл построчно
list_text = file_obj_text.readlines()

print(f'Количество строк в файле: {len(list_text)}')

# Вычисляем количество слов в строке
count_str = 0
for el_str in list_text:
    count_str += 1
    var_num_word = 0
    #  Вычисляем количество слов в строке
    for el_word in el_str.split():
        var_num_word += 1
    # Вывод количества слов
    print(f'Количество слов в {count_str} строке: ', var_num_word)

# Закрытие файла
file_obj_text.close()
