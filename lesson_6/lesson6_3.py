# Класс рабочих
class Worker:
    # Динамические атрибуты
    def __init__(self, name, surname, position, wage, bonus):
        # Имя сотрудника str
        self.name = name
        # Фамилия сотрудника str
        self.surname = surname
        # Должность str
        self.position = position
        # Доход. Защищенный атрибут wage: float; bonus: float
        self._income = {'wage': wage, 'bonus': bonus}


# Класс наследник
class Position(Worker):
    # Метод для получения полного имени сотрудника
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        if self._income.get('wage').isdigit() and self._income.get('bonus').isdigit():
            return float(self._income.get('wage')) + float(self._income.get('bonus'))

        else:
            return 'Ошибка! В показателях дохода присутствует не числовый тип данных'

# Экземпляр класса
worker_Maria = Position('Мария',
                        'Трофимова',
                        'Заместитель директора',
                        '250000',
                        '100000'
                        )

print(f'Полное имя сотрудника: {worker_Maria.get_full_name()}')
print(f'Должность сотрудника: {worker_Maria.position}')
print(f'Общий доход сотрудника равен: {worker_Maria.get_total_income()}')

# Экземпляр класса
worker_Violet = Position(input('Введите имя сотрудника: '),
                         input('Введите фамилию сотрудника: '),
                         input('Введите должность сотрудника: '),
                         input('Введите заработную плату сотрудника: '),
                         input('Введите премию сотрудника: ')
                         )

print(f'Полное имя сотрудника: {worker_Violet.get_full_name()}')
print(f'Должность сотрудника: {worker_Violet.position}')
print(f'Общий доход сотрудника равен: {worker_Violet.get_total_income()}')
