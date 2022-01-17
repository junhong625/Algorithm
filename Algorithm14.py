max_count = 0
max_num = 0
for num in range(1, 1000001):
    count = 0
    num2 = num
    while num2 != 1:
        if num2 % 2 == 0:
            num2 /= 2
            count += 1
        else :
            num2 = num2 * 3 + 1
            count += 1
    if max_count < count:
        max_count = count
        max_num = num
print(max_num)
