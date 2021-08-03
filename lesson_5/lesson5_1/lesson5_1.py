# Открываем файл
file_obj_out = open('text_input_data.txt', 'w', encoding='utf-8')

print('Введите данные в файл. Для окончания процедуры ввода введите пустую строку.')

j = 0
while j == 0:
    var_str_in = input('Введите строку:')
    if var_str_in == '':
        print('Ввод закончен!')
        j = 1
    else:
        file_obj_out.write(var_str_in+'\n')

# Закрытие файла
file_obj_out.close()
