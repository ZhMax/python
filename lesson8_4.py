class Equipment:
    # Динамические атрибуты оборудования,
    # которые являются общими
    def __init__(self, eq_type, name, model, qty):
        # Тип оборудования; str
        self.__eq_type = eq_type
        # Бренд оборудования; str
        self.name = name
        # Название модели оборудования; str
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
        # Разрешение экрана по ширине и высоте; int
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
        # Размер оперативной памяти; int
        self.num_ram = num_ram


# Создание экземпляров классов
obj1_printer_canon = Printer('Canon', 'MF-4410', 150, 'b&w', 'laser')
obj2_printer_canon = Printer('Canon', 'MF443dw', 45, 'color', 'laser')

obj1_printer_hp = Printer('HP', 'M800dn', 150, 'b&w', 'laser')
obj2_printer_hp = Printer('HP', 'CP5210', 45, 'color', 'jet')

obj1_monitor_xiaomi = Monitor('Xiaomi', 'Desktop_monitor', 17, 23.8, 1920, 1080)
obj2_monitor_xiaomi = Monitor('Xiaomi', 'Surface_display', 5, 34, 3440, 1440)

obj1_monitor_aoc = Monitor('AOC', 'Value_Line', 10, 31.5, 2560, 1440)
obj2_monitor_aoc = Monitor('AOC', 'Gaming', 8, 27, 1920, 1080)

obj1_notebook_mac = Notebook('Apple', 'Mac_book_Air', 9, 'Apple_M1', 8, 8)
obj2_notebook_mac = Notebook('Apple', 'Mac_book_Pro', 2, 'Intel_Core_i9', 8, 16)

obj1_notebook_msi = Notebook('MSI', 'Modern', 15, 'AMD_Ryzen_5', 6, 8)
obj2_notebook_msi = Notebook('MSI', 'Creator', 2, 'Intel_Core_i7', 8, 32)
