nums = [int(item) for item in input().split(" ")]
counter = 0
for item in nums:
    if counter % 2 != 0:
        if item % 2 != 0:
            print(f"Index {counter} -> {item}")
    counter += 1
