class Stationery:
    # Динамический атрибут
    def __init__(self, title):
        self.title = title

    # Метод отрисовка
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    # Динамический атрибут
    def __init__(self, title='Pen'):
        super().__init__(title)

    # Перегрузка метода отрисовка
    def draw(self):
        print('\033[3mОтрисовка ручкой\033[0m')


class Pencil(Stationery):
    # Динамический атрибут
    def __init__(self, title='Pencil'):
        super().__init__(title)

    # Перегрузка метода отрисовка
    def draw(self):
        print('\033[1mОтрисовка карандашом\033[0m')


class Handle(Stationery):
    # Динамический атрибут
    def __init__(self, title='Handle'):
        super().__init__(title)

    # Перегрузка метода отрисовка
    def draw(self):
        print('\033[44m\033[37mОтрисовка маркером\033[0m')


# Экземпляр класса Stationery
obj_ink = Stationery('Ink')
obj_ink.draw()

# Экземпляр класса Pen
obj_ink = Pen()
obj_ink.draw()

# Экземпляр класса Pencil
obj_ink = Pencil()
obj_ink.draw()

# Экземпляр класса Handle
obj_ink = Handle()
obj_ink.draw()
