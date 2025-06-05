# def calk1(a, b):
#     return a + b

calk1 = lambda a, b: a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

# math(calk1, 5, 45)
math(lambda a, b: a + b, 5, 45)