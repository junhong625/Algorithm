max_count = 0 # 최장 순환마디의 길이
max_num = 0 # 최장 순환마디의 길이를 가진 수
for num in range(2, 1001): # 2에서 1000까지의 반복문
    r_list = [] #나머지 값이 들어갈 리스트
    r=1 # 처음엔 나눠질 숫자인 1의 역할을 하고 이후부터는 나머지가 입력될 변수
    count = 0 # 몇자리의 순환소수인지 찾기 위한 역할
    for j in range(900): # 몇 번째 나머지까지 찾을 것인지에 대한 범위(**이 범위에 따라서 최대 순환소수를 가진 숫자가 달라진다.)
        while (r < num): # 나머지를 얻어내기 위해서는 나머지가 나누는 숫자보다 커야하기에 나머지인 r이 num보다 커질 때 까지 10을 곱한다.
            r *= 10
        r = r % num # 나머지를 r변수에 입력
        r_list.append(r) # 나머지를 r_list 리스트에 입력
        if (r == 0): # 만약 r(나머지)이 0이면 중단한다.
            break
    for i in range(1, len(r_list)): #  r_list에 들어간 나머지들을 비교한다. 
        if (r_list[0] !=  r_list[i]): # 처음 나머지 값과 같은 나머지 값이 나왔을 때 순환이 끝났다는 의미이기에 다른 나머지 값은 count를 더해준다.
            count += 1
        else: # 같은 나머지 값이 나왔기에 순환이 끝났다는 의미이고 이 때 count가 max_count보다 클 경우에는 max_count와 max_num을 새로 변경해준다.
            if (count > max_count): 
                max_count = count
                max_num = num
            break
print(max_num)