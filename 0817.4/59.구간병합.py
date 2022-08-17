nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
nums = sorted(nums, key=lambda x: x[0])
n_nums = []
s = nums[0][0]
e = nums[0][1]
for i in range(len(nums)):

    if i == 0 or i == 1:
        if e >= nums[i+1][1]:
            e = nums[i+1][1]
            n_nums.extend([[s, e]])
        elif e < nums[i+1][0]:
            e = nums[i][1]
            n_nums.extend([[s, e]])

    elif i != 0:
        if s <= nums[i][0] <= e and s <= nums[i][1] <= e:
            continue
        elif e < nums[i][0]:
            s = nums[i][0]
            e = nums[i][1]
            n_nums.extend([[s, e]])

print(n_nums)
