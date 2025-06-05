transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation_values = list(map(transformation, values))
if values == transformation_values:
    print('OK')
else:
    print('Fail')