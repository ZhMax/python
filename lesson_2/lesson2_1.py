# Список с элементами различных типов данных
var_list = [1, 1.0, complex(1, 1), 'string', ['l', 'i', 's', 't'], (1, 2, 3), set('abc'), {'1': 'Mon', '2': 'Tue'},
            True, bytes(10), None]

# Вывод типа элемента
for var_el in var_list:
    print(type(var_el))

