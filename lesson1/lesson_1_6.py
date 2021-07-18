# Запрашиваем результат в первый день и требуемый результат
num_dist_init = float(input("Введите Ваше расстояние в первый день:"))
num_dist_req = float(input("Введите требуемый результат:"))

num_dist = num_dist_init

# Перемення для количества дней
num_day = 1

print(f"{num_day} день: {num_dist}")
while num_dist < num_dist_req:
    num_dist = num_dist + 0.1 * num_dist
    num_day += 1
    print(f"{num_day} день: {num_dist}")

# Результат расчета
print(f"Требуемый результат будет достигнут на {num_day} день")