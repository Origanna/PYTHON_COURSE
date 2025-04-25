# Самые распространённые ошибки

# SyntaxError (Синтаксическая ошибка)
number_first = 5
number_second = 7
if number_first > number_second: # !!!!! (Изменено: добавлено :)
    print(number_first)
# Отсутствие :

# IndentationError (Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
    print(number_first) # !!!!! (Изменено: добавлен отступ)
# Отсутствие отступов

# TypeError (Типовая ошибка)
text = 'Python'
number = '5' # (Изменено: добавлены '', было 5 без '')
print(text + number)
# Нельзя складывать строки и числа

# ZeroDivisionError (Деление на 0)
number_first = 5
number_second = 1 # (Изменено: был 0 вместо 1)
print(number_first // number_second)
# Делить на 0 нельзя

# KeyError (Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[2]) # (Изменено: было 3 вместо 2)
# Такого ключа не существует

# NameError (Ошибка имени переменной)
name = 'Ivan'
print(name) # (Изменено: было names вместо name)
# Переменной names не существует

# ValueError (Ошибка значения)
text = '555' # (Изменено: было 'Python' вместо 555)
print(int(text))
# Нельзя символы перевести в целые значения