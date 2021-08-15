class Storage:
    # Статический атрибут, ссылающийся на словарь с оборудованием, хранящемся на складе
    storage_dict = {}

    # Классовый метод для добавления оборудования в словарь склада
    @classmethod
    def storage_to(cls, **kwargs):
        strg_dict = cls.storage_dict
        (_, eq_type), (_, name), (_, model), qty, *attr_list = kwargs.items()
        if eq_type in strg_dict.keys():
            if name in strg_dict[eq_type].keys():
                if model in strg_dict[eq_type][name].keys():
                    strg_dict[eq_type][name][model][qty[0]] += qty[1]
                else:
                    # Создаем кортеж из кортежей, содержащих параметры модели
                    # (параметр, значение)
                    model_tuple = qty, *attr_list
                    # Создаем словарь для конкретной модели
                    model_dict = {model: dict(model_tuple)}
                    strg_dict[eq_type][name].update(model_dict)
            else:
                # Создаем кортеж из кортежей, содержащих параметры модели
                # (параметр, значение)
                model_tuple = qty, *attr_list
                # Создаем словарь для конкретной модели
                model_dict = {model: dict(model_tuple)}
                # Создаем словарь для конкретного бренда оборудования
                name_dict = {name: model_dict}
                strg_dict[eq_type].update(name_dict)

        else:
            # Создаем кортеж из кортежей, содержащих параметры модели
            # (параметр, значение)
            model_tuple = qty, *attr_list
            # Создаем словарь для конкретной модели
            model_dict = {model: dict(model_tuple)}
            # Создаем словарь для конкретного бренда оборудования
            name_dict = {name: dict(model_dict)}
            # Создаем словарь для конкретного типа оборудования
            eq_dict = {eq_type: name_dict}
            # Добавляем оборудование к словарю Склада
            strg_dict.update(eq_dict)

        print(f'Оборудование {eq_type} бренда {name} модели {model} в кол-ве {qty[1]} добавлено на склад!')

    # Функция декоратор для проверки
    # корректности данных введеных пользователем
    # при запроса отправки оборудования со склада
    def storage_error_wrapper(func):
        def __wrapper(*args):
            # Проверяем количество аргументов
            if len(args) == 5:
                _, eq_type, name, model, num_out = args
                strg_dict = Storage.storage_dict
                # Проверяем корректность ввода типа оборудования
                if eq_type in strg_dict.keys():
                    # Проверяем корректность ввода бренда оборудования
                    if name in strg_dict[eq_type].keys():
                        # Проверяем корректность ввода модели оборудования
                        if model in strg_dict[eq_type][name].keys():
                            # Проверяем корректность ввода кол-ва
                            if type(num_out) == int:
                                if num_out > 0:
                                    func(Storage, eq_type, name, model, num_out)
                                else:
                                    return print('Кол-во должно быть натуральным числом!')
                            else:
                                return print('Кол-во должно быть числом!')
                        else:
                            return print('Неправильно задана модель оборудования!')
                    else:
                        return print('Неправильно задан бренд оборудования!')
                else:
                    return print('Неправильно задан тип оборудования!')
            else:
                return print('Неправильная формулировка запроса!')
        return __wrapper

    # Классовый метод для отправки оборудования со склада
    @classmethod
    @storage_error_wrapper
    def storage_from(cls, eq_type, name, model, num_out):
        mdl_dict = cls.storage_dict[eq_type][name][model]
        # Имя ключа для количества объектов
        qty_key = list(mdl_dict.keys())[0]
        # Проверка того, что запрашиваемое количество товара имеется на складе
        if mdl_dict[qty_key] >= num_out:
            # Вычитаем кол-во, которое необохимо отправить
            mdl_dict[qty_key] -= num_out
            print(f'Оборудование {eq_type} бренда {name} модели {model} '
                  f'убыло со склада в кол-ве: {num_out}. \n'
                  f'Остаток: {mdl_dict[qty_key]}')
        else:
            print(f'Оборудование {eq_type} бренда {name} модели {model} '
                  f'не может быть отправлено в кол-ве: {num_out}. \n'
                  f'Имеющееся кол-во: {mdl_dict[qty_key]}')


class Equipment:
    # Динамические атрибуты оборудования,
    # которые являются общими
    def __init__(self, eq_type, name, model, qty):
        # Тип оборудования; str
        self.__eq_type = eq_type
        # Бренд оборудования; str
        self.name = name
        # Название оборудования; str
        self.model = model
        # Количество; int
        self.qty = qty


def equip_validation(*args, **kwargs):
    """
    Функция выполняет сравнение типов элемента списка args с типами значений словаря kwargs
    Если тип элемента списка args совпадает с типом значения словаря kwargs,
    то значение приравнивается к элементу списка. В противном случае выводится сообщение.
    Если тип элемента списка args числовой, то выполняется доп. проверка на положительность
    Функция возвращает словарь kwargs с изменненными значениями

    :param args: list
    :param kwargs: dict
    :return: dict
    """

    # Переданный словарь
    var_dict = kwargs
    var_dict_keys = list(var_dict.keys())

    for i in range(0, len(var_dict_keys)):
        # Сравнение типов элемента списка args и значения словаря var_dict
        if isinstance(args[i + 1], type(var_dict[var_dict_keys[i]])):
            # Дополнительная проверка на положительность числовых элементов
            if type(var_dict[var_dict_keys[i]]) == int or type(var_dict[var_dict_keys[i]]) == float:
                if args[i + 1] > 0:
                    var_dict[var_dict_keys[i]] = args[i + 1]
                else:
                    print(f'Неверный числовой атрибут: {var_dict_keys[i]}')
                    break
            else:
                var_dict[var_dict_keys[i]] = args[i + 1]
        else:
            print(f'Неверный тип данных для атрибута: {var_dict_keys[i]}')
            break
    return var_dict


# Класс принтер
class Printer(Equipment):
    # Функция декоратор для проверки, данных введенных пользователем при создании Объекта
    def __printer_error_wrapper(func):
        def __wrapper(*args):
            # Словарь с названием переменных и их базовым значением
            var_dict = {'name': 'N/A', 'model': 'N/A', 'qty': 0, 'color': 'N/A', 'print_type': 'N/A'}
            if len(args) == len(var_dict) + 1:
                func(args[0], **equip_validation(*args, **var_dict))
            else:
                print('Неверное создание объекта класса!')
                func(args[0], **var_dict)
        return __wrapper

    @__printer_error_wrapper
    def __init__(self, name, model, qty, color, print_type, eq_type='Printer'):
        Equipment.__init__(self, eq_type, name, model, qty)
        # Тип принтера: лазерный струйный; str
        self.print_type = print_type
        # Тип печати: цветной или ч/б; str
        self.color = color


# Класс монитор
class Monitor(Equipment):
    # Функция декоратор для проверки, данных введенных пользователем при создании Объекта
    def __monitor_error_wrapper(func):
        def __wrapper(*args):
            # Словарь с названием переменных и их базовым значением
            var_dict = {'name': 'N/A', 'model': 'N/A', 'qty': 0, 'diagonal': 0.0, 'res_w': 0, 'res_h': 0}
            if len(args) == len(var_dict) + 1:
                func(args[0], **equip_validation(*args, **var_dict))
            else:
                print('Неверное создание объекта класса!')
                func(args[0], **var_dict)
        return __wrapper

    @__monitor_error_wrapper
    def __init__(self, name, model, qty, diagonal, res_w, res_h, eq_type='Monitor'):
        Equipment.__init__(self, eq_type, name, model, qty)
        # Размер экрана в дюймах; float
        self.diagonal = diagonal
        # Разрешение экрана по ширине и высоте в пикселах; int
        self.res_w = res_w
        self.res_h = res_h


# Класс ноутбук
class Notebook(Equipment):
    # Функция декоратор для проверки, данных введенных пользователем при создании Объекта
    def __notebook_error_wrapper(func):
        def __wrapper(*args):
            # Словарь с названием переменных и их базовым значением
            var_dict = {'name': 'N/A', 'model': 'N/A', 'qty': 0, 'processor_model': 'N/A', 'num_cores': 0, 'num_ram': 0}
            if len(args) == len(var_dict) + 1:
                func(args[0], **equip_validation(*args, **var_dict))
            else:
                print('Неверное создание объекта класса!')
                func(args[0], **var_dict)
        return __wrapper

    @__notebook_error_wrapper
    def __init__(self, name, model, qty, processor_model, num_cores, num_ram,
                 eq_type='Notebook'):
        Equipment.__init__(self, eq_type, name, model, qty)
        # Модель процессора; str
        self.processor_model = processor_model
        # Количество ядер в процессоре; int
        self.num_cores = num_cores
        # Размер оперативной памятив Гб; int
        self.num_ram = num_ram


# Создание экземпляров классов
obj1_printer_canon = Printer('Canon', 'MF-4410', 150, 'b&w', 'laser')
obj2_printer_canon = Printer('Canon', 'MF443dw', 45, 'color', 'laser')
obj3_printer_canon = Printer('Canon', 'MF-4410', 5, 'color', 'laser')

obj1_printer_hp = Printer('HP', 'M800dn', 85, 'b&w', 'laser')
obj2_printer_hp = Printer('HP', 'CP5210', 63, 'color', 'jet')

obj1_monitor_xiaomi = Monitor('Xiaomi', 'Desktop_monitor', 17, 23.8, 1920, 1080)
obj2_monitor_xiaomi = Monitor('Xiaomi', 'Surface_display', 5, 34.0, 3440, 1440)

obj1_monitor_aoc = Monitor('AOC', 'Value_Line', 10, 31.5, 2560, 1440)
obj2_monitor_aoc = Monitor('AOC', 'Gaming', 8, 27.0, 1920, 1080)
obj3_monitor_aoc = Monitor('AOC', 'Gaming', 2, 27.0, 1920, 1080)

obj1_notebook_mac = Notebook('Apple', 'Mac_book_Air', 9, 'Apple_M1', 8, 8)
obj2_notebook_mac = Notebook('Apple', 'Mac_book_Pro', 2, 'Intel_Core_i9', 8, 16)
obj3_notebook_mac = Notebook('Apple', 'Mac_book_Air', 1, 'Apple_M1', 8, 8)

obj1_notebook_msi = Notebook('MSI', 'Modern', 15, 'AMD_Ryzen_5', 6, 8)
obj2_notebook_msi = Notebook('MSI', 'Creator', 2, 'Intel_Core_i7', 8, 32)

# Заполнение склада
Storage.storage_to(**obj1_printer_canon.__dict__)
Storage.storage_to(**obj2_printer_canon.__dict__)
Storage.storage_to(**obj3_printer_canon.__dict__)
Storage.storage_to(**obj1_printer_hp.__dict__)
Storage.storage_to(**obj2_printer_hp.__dict__)
# print(Storage.storage_dict)

Storage.storage_to(**obj1_monitor_xiaomi.__dict__)
Storage.storage_to(**obj2_monitor_xiaomi.__dict__)
Storage.storage_to(**obj1_monitor_aoc.__dict__)
Storage.storage_to(**obj2_monitor_aoc.__dict__)
Storage.storage_to(**obj3_monitor_aoc.__dict__)
# print(Storage.storage_dict)

Storage.storage_to(**obj1_notebook_mac.__dict__)
Storage.storage_to(**obj2_notebook_mac.__dict__)
Storage.storage_to(**obj3_notebook_mac.__dict__)
Storage.storage_to(**obj1_notebook_msi.__dict__)
Storage.storage_to(**obj2_notebook_msi.__dict__)
print(Storage.storage_dict)


# Отправка товаров со склада
# obj1_printer_canon = Printer('Canon', 'MF-4410', 15, 'b&w', 'laser')
# Storage.storage_to(**obj1_printer_canon.__dict__)

print('Модели принтеров Canon на складе до отправки:')
print(Storage.storage_dict['Printer']['Canon'])
Storage.storage_from('Printer', 'Canon', 'MF-4410', 10)
print('Модели принтеров Canon на складе после отправки:')
print(Storage.storage_dict['Printer']['Canon'])


print('Модели ноутбуков Apple на складе до отправки:')
print(Storage.storage_dict['Notebook']['Apple'])
Storage.storage_from('Notebook', 'Apple', 'Mac_book_Pro', 5)

# Неправильные запросы отправки оборудования
# Storage.storage_from('Scaner', 'Canon', 'MF-4410', 10)
# Storage.storage_from('Printer', 'Xerox', 'MF-4410', 10)
# Storage.storage_from('Printer', 'Canon', 'mf', 10)
# Storage.storage_from('Printer', 'Canon', 'MF-4410', 'ff')
# Storage.storage_from('Printer', 'Canon', 'MF-4410', -10)

# Неправильные запросы создания объектов класса Printer
# obj4_printer_canon = Printer(1, 'MF-4410', 150, 'b&w', 'laser', 2)
# obj4_printer_canon = Printer(1, 'MF-4410', 150, 'b&w', 'laser')
# obj4_printer_canon = Printer('Canon', 'MF-4410', 150, 'b&w', True)
# obj4_printer_canon = Printer('Canon', 'MF-4410', 1.0, 'b&w', True)
# obj4_printer_canon = Printer('Canon', 'MF-4410', -1, 'b&w', True)

# Неправильные запросы создания объектов класса Monitor
# obj3_monitor_xiaomi = Monitor('Xiaomi', 'Desktop_monitor', 17, 23.8, 1920, 1080, 'dd')
# obj3_monitor_xiaomi = Monitor('Xiaomi', 1, 17, 23.8, 1920, 1080)
# obj3_monitor_xiaomi = Monitor('Xiaomi', 'Desktop_monitor', 17, 23.8, 1920, 950.0)

# Неправильные запросы создания объектов класса Notebook
obj4_notebook_mac = Notebook('Apple', 'Mac_book_Pro', 2, 'Intel_Core_i9', 8, 16, 'dwq')
obj4_notebook_mac = Notebook('Apple', 5, 2, 'Intel_Core_i9', 8, 16)
obj4_notebook_mac = Notebook('Apple', 'Mac_book_Pro', 2.4, 'Intel_Core_i9', 8, 16)
obj4_notebook_mac = Notebook('Apple', 'Mac_book_Pro', 2, 8, 8, 16)
obj4_notebook_mac = Notebook('Apple', 'Mac_book_Pro', 2, 'Intel_Core_i9', 'f', 16)
