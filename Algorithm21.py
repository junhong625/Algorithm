def divisor(num):
    sum = 0
    for n in range(1, num):
        if num % n == 0:
            sum += n
    return sum

total = 0
friend_list = []

for num in range(1, 10001):
    if num == divisor(divisor(num)):
        if num != divisor(divisor(divisor(num))):
            if num not in friend_list:
                total += divisor(num) + divisor(divisor(num))
                friend_list.append(divisor(num))

print(total)