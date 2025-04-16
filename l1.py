# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# решетка ctrl k + ctrl c
# открыть ctrl k + ctrl u

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет,', username)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё','ЕЩЁ'))

# text = 'съешь ещё этих мягких французских булок'
# # print(text[0])
# # print(text[1])
# # print(text[len(text)-1])
# # print(text[-1])
# # print(text[-5])
# # print(text[:])
# # print(text[:2])
# # print(text[len(text)-2:])
# # print(text[20:])
# # print(text[2:9])
# # print(text[6:-18])
# # print(text[0:len(text):6])
# # print(text[::6])
# text = text[2:9] + text[-5] + text[:2]
# print(text)