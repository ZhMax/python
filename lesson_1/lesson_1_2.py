#Запрашиваем время в секундах
time_in = int(input("Введите время в секундах:"))

# Определяем часы
time_hour = time_in // 3600

# Определяем минуты
time_calc = time_in - time_hour * 3600
time_min = time_calc // 60

# Определяем секунды
time_calc = time_calc - time_min * 60
time_sec = time_calc

# Выводим результат
time_hour_str = str(time_hour)
time_min_str = str(time_min)
time_sec_str = str(time_sec)

if len(time_hour_str) < 2:
    time_hour_str = "0" + time_hour_str

if len(time_min_str) < 2:
    time_min_str = "0" + time_min_str

if len(time_sec_str) < 2:
    time_sec_str = "0" + time_sec_str

print(f"{time_hour_str}:{time_min_str}:{time_sec_str}")