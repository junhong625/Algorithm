def diagonal_sum(array):
    count = array // 2
    result = 1
    num1 = 1
    num2 = 2
    for i in range(count):
        for j in range(4):
            num1 += num2
            result = result + num1
        num2 += 2
    return result

print('1001 X 1001 대각선 원소의 합 =', diagonal_sum(1001))
