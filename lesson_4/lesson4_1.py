from sys import argv

# Передача данных в программу
charge_script, work_out_param, rate_param, premium_param = argv

# Вычисление заработной платы
res_charge = float(work_out_param) * float(rate_param) + float(premium_param)

# Вывод результата
print(f'Заработная плата: {res_charge}')
