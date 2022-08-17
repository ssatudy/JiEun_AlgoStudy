nums = list(map(int, input().split()))

nums.sort()
zero_sum = []

if nums.count(0) >= 3:
    zero_sum.append([0, 0, 0])
for num in nums:
    if num != 0 and -num in nums:
        zero_sum.extend([num, 0, -num])

    print(zero_sum)



