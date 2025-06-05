# Задание 1.

from functools import reduce

# Исходные списки
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

# Применяем функцию map для возведения в третью степень и округления до трёх знаков после запятой
map_result = list(map(lambda x: round(x ** 3, 3), floats))

# Применяем функцию filter для выбора имён из пяти и более букв
filter_result = list(filter(lambda name: len(name) >= 5, names))

# Применяем функцию reduce для нахождения произведения всех чисел в списке
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

# Вывод результатов
print(map_result)
print(filter_result)
print(reduce_result)
