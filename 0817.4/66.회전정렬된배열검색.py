nums = list(map(int, input().split()))
target = int(input())
for i in range(len(nums)):
    if nums[i] == target:
        result = i
print(result)