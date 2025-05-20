def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False

        i += 1
    if flag:
        return 'Yes'
    else:
        return 'No'
    
n = int(input())
print(prime(n))

# Решение из комментариев (исправленное)
def prime(n):
    if n <= 1:
        return 'No'
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'Yes'
    else:
        return 'No'

n = int(input())
print(prime(n))