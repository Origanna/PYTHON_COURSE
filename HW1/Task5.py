a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
# Меняем значения a и b без использования третьей переменной
a = a + b # Сначала a становится суммой a и b
b = a - b # Затем b становится старым значением a (a + b - b = a)
a = a - b # Наконец, a становится старым значением b (a + b - a = b)
print(a, b)