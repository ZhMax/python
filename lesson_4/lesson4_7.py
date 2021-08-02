def fact_gen(n):
    x = 1
    for j in range(1, n + 1):
        x *= j
        yield x


var_input = input('Введите натуральное число:')
try:
    n = int(var_input)
    if n > 0:
        for el in fact_gen(n):
            print(el)
    else:
        print(f'Число {var_input} не натуральное')
except ValueError:
    print(f'Элемент {var_input} не является числом')