#Запрашиваем число n
num_n = int(input("Введите целое положительное число n:"))

#Составляем комбинации nn и nnn
num_nn = int(str(num_n) + str(num_n))
num_nnn = int(str(num_nn) + str(num_n))

#Выводим на экран, полученные комбинации
print(f"{num_n}, {num_nn}, {num_nnn}")

#Выводим на экран сумму комбинаций
print(f"Сумма комбинаций: n + nn + nnn = {num_n+num_nn+num_nnn}")