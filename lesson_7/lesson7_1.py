from random import randint


def mat_creation(size_row, size_column):
    """
    Функция, создающая список из size_row списков длины size_column,
    заполненных целыми числами

    :param size_row: количество списков (строки матрицы); int > 0
    :param size_column: количество элементов в
    каждом списке (столбцы матрицы); int > 0
    :return: список из size_row списков длины size_column; list
    """

    res_mat = []
    if size_row > 0 and size_column > 0:
        for i in range(0, size_row):
            var_column = [randint(-9, 9) for j in range(0, size_column)]
            res_mat.append(var_column)
        return res_mat
    else:
        return 'Задан неправильный размер матрицы'


class MatrixClass:
    def __init__(self, mat_list):
        self.mat_list = mat_list

    def __str__(self):
        # Вычисляем максимальное количество символов в числах каждого столбца матрицы,
        # чтобы затем добавить необходимое количество пробелов для выравнивания по вертикали
        var_str = ''
        mat_input = self.mat_list
        # Массив с максимальным количеством символов в числах каждого столбца матрицы
        max_el_len = []
        for j in range(0, len(mat_input[0])):
            el_len = []
            # Вычисляем количество символов в каждом числе столбца
            for i in range(0, len(mat_input)):
                el_len.append(len(str(mat_input[i][j])))
            # Находим максимальное количество символов
            max_el_len.append(max(el_len))
        # Создаем строку, отбражающую матрицу в виде таблицы
        # Добавляем необходимое количество пробелов перед числами для выравнивания по вертикали,
        # исходя из максимального количество символов max_el_len[j] в числах каждого столбца
        for mat_row in self.mat_list:
            for j in range(0, len(mat_row)):
                var_str += ' ' + (max_el_len[j]-len(str(mat_row[j])))*' ' + str(mat_row[j])
            var_str += '\n'
        # Выводим результат
        return var_str

    def __add__(self, other):
        row_size = len(self.mat_list)
        column_size = len(self.mat_list[0])
        # Проверяем, что размер складываемых матрицы совпдает
        if row_size == len(other.mat_list) and column_size == len(other.mat_list[0]):
            # Матрица суммы
            res_mat = []
            # Выполняем сложение матрицы построчно
            for a_list, b_list in zip(self.mat_list, other.mat_list):
                # Вычисляем сумму элементов в каждой строке
                var_list = [a_el + b_el for a_el, b_el in zip(a_list, b_list)]
                res_mat.append(var_list)
            return MatrixClass(res_mat)
        else:
            return 'Задан неверный размер матриц'


# Создаем матрицу a как список списков
mat_a = mat_creation(2, 3)
print(mat_a)
# Создаем матрицу b как список списков
mat_b = mat_creation(2, 3)
print(mat_b)

# Создаем матрицу a как объект
obj_mat_a = MatrixClass(mat_a)
print('A = ')
print(obj_mat_a)

# Создаем матрицу b как объект
obj_mat_b = MatrixClass(mat_b)
print('B  = ')
print(obj_mat_b)

# Выполняем сложение матриц a и b
print('A + B = ')
print(obj_mat_a + obj_mat_b)
