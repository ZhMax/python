var_str = input("Введите строку из нескольких слов, разделенных пробелами:")

# Убираем лишние пробелы
while var_str.find('  ') > -1:
    var_str = var_str.replace('  ', ' ')

# Разбиваем строку на слова по разделителю
var_list = var_str.split(' ')

# Нумеруем слова в списке
var_list_enum = list(enumerate(var_list))

# Выводим результат
for i in range(0, len(var_list_enum)):
    print(f"{int(var_list_enum[i][0])+1}: {var_list_enum[i][1]:.10}")
