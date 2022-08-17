nums = list(map(int, input().split()))
target = int(input())
s = 0
e = len(nums)-1

while s <= e:
    m = (s+e) // 2
    if nums[m] == target:
        result = m
        break
    elif nums[m] < target:
        s = m + 1
    elif nums[m] > target:
        e = m - 1

print(m)