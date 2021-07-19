# Запрашиваем число n
num_n = int(input("Введите целое положительное число n:"))

# Определяем максимальную цифру
num_n_int_part = num_n
num_n_dig_max = 0

while num_n_int_part > 0:
    # Определяем цифру на текущем разряде: abc % 10 = c
    num_n_mod = num_n_int_part % 10
    # Сравниваем остаток с максимальной цифрой: c > dig_max ?
    if num_n_mod > num_n_dig_max:
        num_n_dig_max = num_n_mod
    # Переходим к следующему разряду: abc // 10 = ab
    num_n_int_part = num_n_int_part // 10

print(f"Максимальная цифра в числе: {num_n_dig_max}")
