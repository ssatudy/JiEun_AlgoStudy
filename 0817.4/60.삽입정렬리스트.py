nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    j = i
    while j > 0 and nums[j - 1] > nums[j]: # for문을 두번 쓰는 것 방식보다 불필요한 작업을 줄여줌 .
        nums[j - 1], nums[j] = nums[j], nums[j - 1]
        j -= 1
print(nums)