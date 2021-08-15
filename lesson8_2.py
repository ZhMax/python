# Класс-исключение
class DivError(Exception):
    def __init__(self, txt):
        self.txt = txt


# Запрос чисел
print('Расчет отношения a к числу b')
str_a, str_b = input('Введите число a: '), input('Введите число b: ')

try:
    a = float(str_a)
    b = float(str_b)
    # Проверка равенства знаменталя нолю
    if b == 0:
        raise DivError('Деление на ноль!')
except ValueError:
    print('Введено не число!')
except DivError as err:
    print(err)
else:
    # Результат деления
    print(f'Данные прошли проверку! Результат деления {a} / {b} = {a / b}')
