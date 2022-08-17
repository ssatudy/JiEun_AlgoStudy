nums = list(map(int, input().split()))
target = int(input())
s = 0
e = 1
for i in range(len(nums)):
    if nums[s] + nums[e] == target:
        result = [s+1, e+1]
    elif nums[s] + nums[e] < target:
        e += 1
    elif nums[s] + nums[e] > target and s < e:
        s += 1
        e -= 1
    elif nums + nums[e] > target and s == e:
        s -= 1

result = [s+1, e+1]
print(result)