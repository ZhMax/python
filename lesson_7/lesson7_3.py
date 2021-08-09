class Cell:
    def __init__(self, num_unit):
        # Динамический атрибут,
        # определяющий количество ячеек в клетке; int
        if type(num_unit) == int:
            if num_unit > 0:
                self.num_unit = num_unit
            else:
                print('Клетки не существует!')
                self.num_unit = 0
        else:
            print('Неправильно задано количество ячеек!')
            self.num_unit = 0

    # Вывод клетки на экран
    def __str__(self):
        return self.num_unit * '*'

    # Функция декоратор для проверки
    # принадлежности второго аргумента функции классу Cell
    def __error_wrapper(func):
        def __wrapper(var_a, var_b):
            # Проверяем принадлежит ли второй аргумент классу Cell
            if isinstance(var_b, Cell):
                return func(var_a, var_b)
            else:
                return 'Неправильный вызов операции!'
        return __wrapper

    # Метод сложения двух клеток
    @__error_wrapper
    def __add__(self, other):
        return Cell(self.num_unit + other.num_unit)

    # Метод вычитания двух клеток
    @__error_wrapper
    def __sub__(self, other):
        res_num_unit = self.num_unit - other.num_unit
        return Cell(res_num_unit) if res_num_unit > 0 else 'Разность клеток не определена!'

    # Метод умножения двух клеток
    @__error_wrapper
    def __mul__(self, other):
        return Cell(self.num_unit * other.num_unit)

    # Метод деления двух клеток
    @__error_wrapper
    def __truediv__(self, other):
        res_num_unit = self.num_unit // other.num_unit
        return Cell(res_num_unit) if res_num_unit > 0 else 'Деление клеток не определено!'

    # Вывод структуры клетки в заданном формате
    def make_order(self, el_in_row):
        if type(el_in_row) == int:
            if el_in_row > 0:
                # # Вывод структуры клетки посредством работы с элементами строки и символом *
                # # Определяем количество ячеек в клетке
                # len_str_cell = self.num_unit
                # # Определяем разбиение ячеек в зависисмости от el_in_row
                # # Количество полных строк
                # var_div_int = len_str_cell // el_in_row
                # # Количество ячеек в не полной строке
                # var_mod_int = len_str_cell % el_in_row
                # # Результирующая строка
                # res_str = ''
                # # Формируем структуру строки
                # for i in range(0, var_div_int-1):
                #     res_str += el_in_row * '*' + '\n'
                # if var_mod_int == 0:
                #     res_str += el_in_row * '*'
                # else:
                #     res_str += el_in_row * '*' + '\n' + var_mod_int * '*'
                # return res_str

                # Вывод структуры клетки посредством работы с элементами класса Cell и строками
                # Определяем разбиение ячеек в зависисмости от el_in_row
                count_num = self.num_unit // el_in_row
                if count_num > 0:
                    # Создаем клетку с кол-ом ячеек el_in_row
                    var_cell = Cell(el_in_row)
                    # Создаем результирующую строку из строк клетки var_cell
                    res_str = '\n'.join([str(var_cell) for i in range(0, count_num)])
                    # Добавляем к строке остаток от деления клетки self на клетку var_cell
                    if self.num_unit % el_in_row > 0:
                        res_str += '\n' + str(self - Cell(count_num) * var_cell)
                        return res_str
                    else:
                        return res_str
                else:
                    res_str = str(self)
                    return res_str
            else:
                return 'Неправильный вызов операции!'
        else:
            return 'Неправильный вызов операции!'


# Объекты класса клетка
a_cell = Cell(2)
b_cell = Cell(3)
c_cell = Cell(0)
print(f'Клетка a имеет вид: {a_cell}')
print(f'Клетка b имеет вид: {b_cell}')
print(f'a + b = {a_cell + b_cell}')
print(f'a + 3 = {a_cell + 3}')
print(f'a - b = {a_cell - b_cell}')
print(f'b - a = {b_cell - a_cell}')
print(f'a * b = {a_cell * b_cell}')
print(f'a / b = {a_cell / b_cell}')
print(f'b / a = {b_cell / a_cell}')

print('Метод .make_order(2) для a + b:')
print((a_cell + b_cell).make_order(2))
print('Метод .make_order(3) для a * b:')
print((a_cell * b_cell).make_order(3))
print('Метод make_order(5) для a:')
print(a_cell.make_order(2))

print('Метод make_order(0) для a:')
print(a_cell.make_order(0))
