num = 1
num2 = 0
measure_count = 0
while measure_count < 500:
    measure_count = 0
    num2 += num
    for i in range(1, num2+1):
        if num2 % i == 0:
            measure_count += 1
    num += 1
    print(num2, '|', measure_count)
print(num2)
