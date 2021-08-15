class Storage:
    # Статический атрибут, ссылающийся на словарь с оборудованием, хранящемся на складе
    storage_dict = {}

    # Классовый метод для добавления оборудования в словарь склада
    @classmethod
    def storage_to(cls, **kwargs):
        strg_dict = cls.storage_dict
        (_, eq_type), (_, name), (_, model), qty, *attr_list = kwargs.items()
        # print(eq_type, name, model, qty, *attr_list)
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

    # Классовый метод для отправки оборудования со склада
    @classmethod
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


# Класс принтер
class Printer(Equipment):
    def __init__(self, name, model, qty, color, print_type, eq_type='Printer'):
        Equipment.__init__(self, eq_type, name, model, qty)
        # Тип принтера: лазерный струйный; str
        self.print_type = print_type
        # Тип печати: цветной или ч/б; str
        self.color = color


# Класс монитор
class Monitor(Equipment):
    def __init__(self, name, model, qty, diagonal, res_w, res_h, eq_type='Monitor'):
        Equipment.__init__(self, eq_type, name, model, qty)
        # Размер экрана в дюймах; float
        self.diagonal = diagonal
        # Разрешение экрана по ширине и высоте в пикселах; int
        self.res_w = res_w
        self.res_h = res_h


# Класс ноутбук
class Notebook(Equipment):
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
obj2_monitor_xiaomi = Monitor('Xiaomi', 'Surface_display', 5, 34, 3440, 1440)

obj1_monitor_aoc = Monitor('AOC', 'Value_Line', 10, 31.5, 2560, 1440)
obj2_monitor_aoc = Monitor('AOC', 'Gaming', 8, 27, 1920, 1080)
obj3_monitor_aoc = Monitor('AOC', 'Gaming', 2, 27, 1920, 1080)


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
# print(Storage.storage_dict)


# Отправка товаров со склада
print('Модели принтеров Canon на складе до отправки:')
print(Storage.storage_dict['Printer']['Canon'])
Storage.storage_from('Printer', 'Canon', 'MF-4410', 10)
print('Модели принтеров Canon на складе после отправки')
print(Storage.storage_dict['Printer']['Canon'])

print('Модели ноутбуков Apple на складе до отправки:')
print(Storage.storage_dict['Notebook']['Apple'])
Storage.storage_from('Notebook', 'Apple', 'Mac_book_Pro', 5)

