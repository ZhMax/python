from abc import ABC, abstractmethod


# Абстрактный класс одежда,
# задающий интерфейс для классов наследников
class Clothes:

    def __init__(self, param):
        # Динамический параметр для рассматриваемого типа одежды; float
        if type(param) == float or type(param) == int:
            self.param = param
        else:
            print('Неверно задан параметр!')
            quit()

    # Заготовка по метод вычисиляющий количества ткани
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    # Декоратор @property для преобразования метода в атрибут
    @property
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    def fabric_consumption(self):
        return 2 * self.param + 0.3


# Объект класса Пальто
coat_obj = Coat(3.1)
print(f'Для пошива пальто потребуется {coat_obj.fabric_consumption} ткани')

# Объект класса Костюм
suit_obj = Suit(1.69)
print(f'Для пошива костюма потребуется {suit_obj.fabric_consumption()} ткани')

print(f'Общий расход ткани {coat_obj.fabric_consumption + suit_obj.fabric_consumption()}')
