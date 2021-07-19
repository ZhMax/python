# Запрашиваем время в секундах
time_in = int(input("Введите время в секундах:"))

# Определяем часы
time_hour = time_in // 3600

# Определяем минуты
time_calc = time_in % 3600
time_min = time_calc // 60

# Определяем секунды
time_calc = time_calc % 60
time_sec = time_calc

# Выводим результат
print("{:02d}:{:02d}:{:02d}".format(time_hour, time_min, time_sec))
