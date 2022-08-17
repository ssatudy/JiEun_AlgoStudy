nums =[1, 2, 3, 4]

multi_list = []

multi = 1
for i in range(len(nums)):
    multi_list.append(multi)
    multi *= nums[i]

multi = 1
for i in range(len(nums)-1, -1 ,-1):
    multi_list[i] *= multi
    multi *= nums[i]

print(multi_list)



