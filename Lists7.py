data_list = list(map(int, input().split(" ")))

positive_nums = list(filter(lambda x: x > 0, data_list))
index = 0
if not positive_nums == []:
    for el in range(0, len(positive_nums)):
        last_element = positive_nums.pop()
        positive_nums.insert(index, last_element)
        index += 1

    print(*positive_nums)
    
else:
    print("empty")
