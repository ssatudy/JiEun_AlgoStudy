nums = [1, 4, 2, 3]

nums.sort()
sum_list = []
for i in nums[::2]:
    sum_list.append(i)
print(sum(sum_list))

'''
for문 없이 계산하기 => sum(sorted(nums)[::2])
'''

