list_1 = [0, -1, 5, 2, 3]

count = 0

for i in range(1, len(list_1)):
    if list_1[i] > list_1[i-1]:
        print(f"({list_1[i-1]} < {list_1[i]})")
        count +=1
print(count)