n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(1, n):
    j = i
    while j > 0 and nums[j-1] > nums[j]:
        nums[j-1], nums[j] = nums[j], nums[j-1]
        j -= 1

print(*nums, sep='\n')
