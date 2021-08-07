from itertools import cycle
import time


class TrafficLight:
    # Статический атрибут со всеми цветами светофора и продолжительностью их отображения
    __dict_color = {'красный': ['\033[31m\033[41mЦвет\033[0m', 7],
                  'желтый': ['\033[33m\033[43mЦвет\033[0m', 2],
                  'зеленый': ['\033[32m\033[42mЦвет\033[0m', 10]}

    # Динамический атрибут с цветом светофора при создании экземпляра
    def __init__(self, color):
        # Текущий цвет светорфора; str
        self.__color = color

    # Метод, реализующий переключение цветов светофора
    def running(self):
        if self.__color in self.__dict_color.keys():
            # Итератор ключей с цветами светофора
            iter_color = cycle(self.__dict_color.keys())
            # Текущий цвет светофора
            current_color = self.__color
            # Счетчик повторений полных циклов работы светофора
            count = 0
            # Цикл по элементам итератора
            for var_color in iter_color:
                # Если элемент итератора равен текущему цвету выводим сигнал светофора на экран
                if var_color == current_color:
                    print(self.__dict_color.get(var_color)[0])
                    time.sleep(self.__dict_color.get(var_color)[1])
                    # После отображения меняем текущий цвет светофора на следующий
                    current_color = next(iter_color)
                    # Считаем количество полныъ циклов работы светофора
                    count += 1 if current_color == self.__color else 0
                # Если количество полных циклов работы светофора равно 2 прекращаем его работу
                if count == 2:
                    print('Светофор завершил работу')
                    break
        else:
            print('Введен неправильный цвет светофора')


# Создаем объект класса
obj_trafficlight = TrafficLight('желтый')
# Вызываем метод, выполняющий переключение светофора
obj_trafficlight.running()
