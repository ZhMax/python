import json

# Открываем файл и считываем данные
with open('text_firms.txt', 'r', encoding='utf-8') as file_text_in:
    # Определяем список из кортежей с названием фирм и их данных
    list_firm_data = []
    for str_firm in file_text_in.readlines():
        # Создаем строку из названий фирм и список из их показателей
        list_firm_name, list_firm_indicators = (str_firm.split()[0], str_firm.split()[1:])
        # Вычисляем величину прибыли
        var_prod = float(list_firm_indicators[1]) - float(list_firm_indicators[2])
        # Добавляем данные в список
        list_firm_data.append((list_firm_name, var_prod))

    print('Название фирмы и величина прибыли:')
    print(list_firm_data)

# Расчет средней прибыли без учета убыточных компаний
var_sum = 0
var_num_positive = 0
for el in list_firm_data:
    if el[1] > 0:
        var_sum += el[1]
        var_num_positive += 1

aver_prof = var_sum / var_num_positive if var_num_positive > 0 else 'Прибыльные компании отсутствуют'

# Создание списка из словарей
list_analytics = [dict(list_firm_data), {'Average_profit': aver_prof}]
print('Список из словарей:')
print(list_analytics)

# Сериализация к JSON формату
with open('firm_analytics.json', 'w') as file_json_analytics:
    json.dump(list_analytics, file_json_analytics)
