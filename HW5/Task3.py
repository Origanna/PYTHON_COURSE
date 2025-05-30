# Задание 3.
def my_sum(*args):
    total_sum = 0 # Инициализация переменной для хранения суммы

    for i_elem in args:
        # Проверка, является ли элемент целым числом
        if isinstance(i_elem, int):
            total_sum += i_elem # Добавление числа к общей сумме
        # Проверка, является ли элемент списком или кортежем
        elif isinstance(i_elem, (list, tuple)):
            # Рекурсивный вызов функции для суммирования элементов внутри списка или кортежа
            for x in i_elem:
                total_sum += my_sum(x)
    return total_sum

# Основной код для тестирования
# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, 2, 3, 4, 5))