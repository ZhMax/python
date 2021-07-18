# Запрашиваем величины издержек и выручки
num_proceeds = float(input("Введите выручку фирмы:"))
num_expense = float(input("Введите издержки фирмы:"))

if num_proceeds > num_expense:
    print("Фирма работает в прибыль")
    # Величина прибыли
    num_profit = num_proceeds - num_expense
    # Рентабельность
    num_eff = num_profit / num_proceeds
    print(f"Рентабельность фирмы: {num_eff}")
    num_staff = float(input("Введите количество сотрудников:"))
    num_profit_staff = num_profit / num_staff
    print(f"Прибыль на одного сотрудника: {num_profit_staff}")
elif num_proceeds == num_expense:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")