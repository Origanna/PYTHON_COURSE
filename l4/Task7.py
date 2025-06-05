# colors = ['red', '8898', 'blue']
# data = open('file.txt', 'a') # Здесь указываем режим, в котором будем работать.
# data.writelines(colors) # Разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# print(56)

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()