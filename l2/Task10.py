dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '<='
print(dictionary['left']) # <=
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
    # up: ↑
    # down: ↓
    # right: →
    print(item)
    # up
    # down
    # right
for (k,v) in dictionary.items():
    print(k,v)
print(dictionary.items())
dictionary[895] = 98998
print(dictionary)