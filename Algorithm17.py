count = 0
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
for ten in tens: ## 1~19까지 들어있는 nums에 20~99까지 숫자 영어로 변환해서 추가
    nums.append(ten)
    for idx in range(9):
        nums.append(str(ten + nums[idx]))

for hun in range(9): ## 1~99까지 들어있는 nums에 100~999까지 숫자 영어로 변환해서 추가
    nums.append(str(nums[hun]) + 'hundred')
    for hund in range(0, 99):
        nums.append(str(nums[hun] + 'hundredand' + nums[hund]))

nums.append('onethousand')

for num in nums:
    count += len(num)

print(count)
