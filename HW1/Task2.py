# Задание 2.
# Ввод количества минут
minutes = int(input('Введите количество минут: '))
# Вычисление количества полных часов
hours = minutes // 60
# Вычисление оставшихся минут
rest_minutes = minutes % 60
# Вывод результатов
print('Часов:', hours)
print('Осталось минут:', rest_minutes)