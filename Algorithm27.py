def prime_num(num):
    if num < 2:
        return False

    # 제곱근 통해 소수 확인
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


max_prime_number_count = 0
A = 0
# 소수
B = 0
for a in range(-999, 1000):
    # a는 홀수
    if a % 2 == 0:
        continue
    for b in range(-999, 1000):
        # b는 소수여야함
       if prime_num(b):
            x = 0
            while True:
                if prime_num(x*x+a*x+b):
                    x += 1
                else:
                    break
                if max_prime_number_count < x:
                    max_prime_number_count = x
                    A, B = a, b
print("소수의 최대 연속 횟수 :", max_prime_number_count)
print("a = %d, b = %d" % (A, B))
print("계수 a와 b의 곱 :", A*B)
