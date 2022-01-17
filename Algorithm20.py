def factorial_sum(num):
    sum, total = 1, 0
    for n in range(num, 1, -1):
        sum *= n
    for idx in range(len(str(sum))):
        total += int(str(sum)[idx])
    return total
print(factorial_sum(100))
