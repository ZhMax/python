class Road:
    # Статический атрибут экземпляра
    # Плотность асфальта в кг / м / м / см; float
    rho_asphalt = 25

    # Динамические атрибуты экземпляра
    def __init__(self, length, width, thickness):
        # длина покрытия в м (защищенный атрибут); float
        self._length = length
        # ширина покрытия в м (защищенный атрибут); float
        self._width = width
        # толщина покрытия в см (защищенный атрибут); float
        self._thickness = thickness

    # Метод для вычисления массы асфальта
    def mass_asphalt(self):
        # Проверка того, что входные данные числовые
        # Подсчет массы асфальта
        if self._length.isdigit() and self._thickness.isdigit() and self._thickness.isdigit():
            return True, float(self._length) * float(self._width) * float(self._thickness) * self.rho_asphalt
        else:
            print('Введены не числовой тип данных!')
            return False, 1


# Создание экземпляра класса
road_perm_ilinsk = Road(input('Длина дорожного полотна в м:'),
                        input('Ширина дорожного полотна в м:'),
                        input('Толщина асфальтового покрытия в см:')
                        )

# Вывод результата
if road_perm_ilinsk.mass_asphalt()[0]:
    print(f'Для данного дорожного полотна потребуется {road_perm_ilinsk.mass_asphalt()[1] / 1000} т асфальта')
