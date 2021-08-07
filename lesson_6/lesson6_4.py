# Класс автомобилей
class Car:
    # Статический атрибут
    # Направление поворота
    __dict_direction = {'r': 'направо', 'l': 'налево'}

    # Динамические атрибуты класса
    def __init__(self, speed, color, name, is_police):
        # Скорость автомобиля в км/ч; str
        self.speed = speed
        # Цвет автомобиля; str
        self.color = color
        # Марка автомобиля; str
        self.name = name
        # Является ли автомобиль полийцеским; bool
        self.is_police = is_police

    # Сообщение, что автомобиль поехал
    def go(self):
        print(f'Автомобиль {self.name} поехал вперед')

    # Сообщение, что автомобиль остановился
    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    # Сообщение, что автомобиль повернул
    def turn(self, direction):
        # Проверяем соответствует ли введенные данные запрашиваемым комнадам
        if direction in self.__dict_direction.keys():
            print(f'Автомобиль {self.name} повернул {self.__dict_direction.get(direction)}')
        else:
            print('Неверный ввод данных!')

    # Текущая скорость автомобиля
    def show_speed(self):
        # Проверяем является ли введенная скорость числом
        if self.speed.isdigit():
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')
        else:
            print('Неверный ввод данных!')

    # Проверка является ли автомобиль полицейским
    def police_check(self):
        if self.is_police:
            print(f'Автомобиль {self.name} - полицейский')
        else:
            print(f'Автомобиль {self.name} - гражданский')


class TownCar(Car):
    # Динамические атрибуты класса TownCar
    def __init__(self, speed, color, name, type_car, is_police=0):
        # Передаем атрибуты в класс Car
        Car.__init__(self, speed, color, name, is_police)
        # Тип автомобиля, напр. кроссовер, седан и т.д.; str
        self.type_car = type_car

    def show_speed(self):
        # Проверяем является ли введенная скорость числом
        if self.speed.isdigit():
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')
            # Проверяем превышает ли скорость предельно допустимую
            if float(self.speed) > 60:
                print(f'Скорость {self.name} превышает предельно допустимую в 60 км/ч!')
        else:
            print('Неверный ввод данных!')


class WorkCar(Car):
    # Динамические атрибуты класса WorkCar
    def __init__(self, speed, color, name, purpose_car, is_police=0):
        # Передаем атрибуты в класс Car
        Car.__init__(self, speed, color, name, is_police)
        # Назначение автомобиля, напр. грузовик, самосвал, подъемный кран; str
        self.purpose_car = purpose_car

    def show_speed(self):
        # Проверяем является ли введенная скорость числом
        if self.speed.isdigit():
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')
            # Проверяем превышает ли скорость предельно допустимую
            if float(self.speed) > 40:
                print(f'Скорость {self.name} превышает предельно допустимую в 40 км/ч!')
        else:
            print('Неверный ввод данных!')


class SportCar(Car):
    # Динамические атрибуты класса SportCar
    def __init__(self, speed, color, name, time_acceleration, is_police=0):
        # Передаем атрибуты в класс Car
        Car.__init__(self, speed, color, name, is_police)
        # Время разгона от 0 до 100 км/ч; float
        self.time_acceleration = time_acceleration


class PoliceCar(Car):
    # Динамические атрибуты класса PoliceCar
    def __init__(self, speed, color, name, police_division):
        # Передаем атрибуты в класс Car
        Car.__init__(self, speed, color, name, 1)
        # Подразделение полиции
        self.police_division = police_division


# Экземпляр класса
car_Mazda = TownCar('80', 'Коричневый', 'Mazda', 'Кроссовер')

# Вывод атрибутов
print(f'Автомобиль: {car_Mazda.name}; '
      f'цвет: {car_Mazda.color}; '
      f'скорость: {car_Mazda.speed}; '
      f'тип: {car_Mazda.type_car}')
car_Mazda.police_check()
car_Mazda.show_speed()

# Методы экземпляра
car_Mazda.go()
car_Mazda.stop()
car_Mazda.turn(input('Чтобы автомобиль повернул направо введите R, повернул налево введите L: ').lower())


# Экземпляр класса
car_Cat = TownCar('35', 'Желтый', 'Caterpillar', 'Колесный погрузчик')

# Вывод атрибутов
print(f'Автомобиль: {car_Cat.name}; '
      f'цвет: {car_Cat.color}; '
      f'скорость: {car_Cat.speed}; '
      f'назначение: {car_Cat.type_car}')
car_Cat.police_check()
car_Cat.show_speed()

# # Методы экземпляра
# car_Cat.go()
# car_Cat.stop()
# car_Cat.turn(input('Чтобы автомобиль повернул направо введите R, повернул налево введите L: ').lower())

# Экземпляр класса
car_Porsche = SportCar('190', 'Красный', 'Porsche 911', '3 с')

# Вывод атрибутов
print(f'Автомобиль: {car_Porsche.name}; '
      f'цвет: {car_Porsche.color}; '
      f'скорость: {car_Porsche.speed}; '
      f'Разгон до 100 км/ч: {car_Porsche.time_acceleration}')
car_Porsche.police_check()
car_Porsche.show_speed()

# # Методы экземпляра
# car_Porsche.go()
# car_Porsche.stop()
# car_Porsche.turn(input('Чтобы автомобиль повернул направо введите R, повернул налево введите L: ').lower())

# Экземпляр класса
car_Skoda = PoliceCar('100', 'Синий', 'Skoda', 'ДПС')

# Вывод атрибутов
print(f'Автомобиль: {car_Skoda.name}; '
      f'цвет: {car_Skoda.color}; '
      f'скорость: {car_Skoda.speed}; '
      f'подразделение: {car_Skoda.police_division}')
car_Skoda.police_check()
car_Skoda.show_speed()

# Методы экземпляра
# car_Skoda.go()
# car_Skoda.stop()
# car_Skoda.turn(input('Чтобы автомобиль повернул направо введите R, повернул налево введите L: ').lower())