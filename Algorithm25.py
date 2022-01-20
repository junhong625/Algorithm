# 피보나치 수열에서 처음으로 1000자리가 되는 항은 몇 번째?

def F(maximum):
    num1 = 1
    num2 = 0
    count = 1
    while True:
        num2 += num1
        count += 1
        if len(str(num2)) >= maximum:
            return count
            break
        num1 += num2
        count += 1
        if len(str(num1)) >= maximum:
            return count
            break
F(1000)