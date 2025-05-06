list1 = [5, 4, 6, 7, -10]
k = int(input())
k = k % len(list1)

list_res = []

for i in range(k):
    list_res.append(list1[len(list1) - 1 - i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])
print(list_res)

# Другой вариант решения из комментариев, но список не выводится...
# n = int(input("Введите количество чисел: ")) # Вводим количество чисел в списке
# numbers = [] # Задаем пустой список

# for i in range(n):
#     num = int(input(f"Введите число {i+1}: "))
# numbers.append(num) # Цикл для того чтобы пользователь сам задал нужный ему список

# k = int(input("Введите сдвиг вправо (число): ")) # Просим пользователя выбрать на какое количество чисел сделать сдвиг
# if k < 0: # Проверяем, является ли К положительным числом
#     print("Ошибка! Сдвиг должен быть положительным числом!")
#     exit()

# numbers_copy = numbers.copy() # Создаем копию списка

# for i in range(len(numbers)):
#     numbers[(i + k) % len(numbers)] = numbers_copy[i] # Цикл, который берет элемент из копии, и ставит его на место в оригинальном списке, таким образом происходит сдвиг

# print(numbers) # Выводим список