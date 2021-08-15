class ComplexNum:
    def __init__(self, num_re, num_im=0):
        self.num_re = num_re
        self.num_im = num_im

    def __str__(self):
        if self.num_re and self.num_im > 0:
            return str(self.num_re) + '+' + str(self.num_im)+'i'
        if self.num_im == 0:
            return str(self.num_re)
        if self.num_re == 0:
            return str(self.num_im)+'i'
        if self.num_im < 0:
            return str(self.num_re) + str(self.num_im) + 'i'

    # Функция декоратор для проверки
    # принадлежности второго аргумента функции классу ComplexNum либо
    # принадлежности классам float или int
    def __error_wrapper(func):
        def __wrapper(var_a, var_b):
            # Проверяем принадлежит ли второй аргумент классу ComplexNum
            if isinstance(var_b, ComplexNum):
                return func(var_a, var_b)
            elif isinstance(var_b, float) or isinstance(var_b, int):
                return func(var_a, ComplexNum(var_b))
            else:
                return 'Неправильный вызов операции!'
        return __wrapper

    @__error_wrapper
    def __add__(self, other):
        return ComplexNum(self.num_re + other.num_re, self.num_im + other.num_im)

    @__error_wrapper
    def __mul__(self, other):
        res_re = self.num_re * other.num_re - self.num_im * other.num_im
        res_im = self.num_re * other.num_im + self.num_im * other.num_re
        return ComplexNum(res_re, res_im)


# Экземпляры класса комплексных чисел
a_compnum = ComplexNum(2, -2)
b_compnum = ComplexNum(-1, 4)
c_compnum = ComplexNum(0, 5)
print(f'a = {a_compnum}, b = {b_compnum}, c = {c_compnum}')
print(f'a + b = {a_compnum + b_compnum}')
print(f'a + c = {a_compnum + c_compnum}')
print(f'a + 3 = {a_compnum + 3}')
print(f'a + 5.32 = {a_compnum + 5.32}')
print(f'a + "string" = {a_compnum + "fw"}')

print(f'a * b = {a_compnum * b_compnum}')
print(f'a * c = {a_compnum * c_compnum}')
print(f'a * 3 = {a_compnum * 3}')
print(f'a * 5.32 = {a_compnum * 5.32}')
print(f'a * "string" = {a_compnum * "fw"}')