nums = list(map(int, input().split()))
color = [0, 1, 2]
n_nums = []

# 0 1 2 순서대로 n_nums 에 넣기

for i in range(len(color)):
    for j in range(len(nums)):
        if color[i] == nums[j]:
            n_nums.append(nums[j])
        else:
            continue
print(n_nums)