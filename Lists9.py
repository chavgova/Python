data_list = list(map(int, input().split(" ")))

data_list.sort()
print(data_list[0], end='')
del data_list[0]
for element in data_list:
    print(" <= ", end='')
    print(element, end='')

print()
