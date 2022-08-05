from operator import index

# test num
#nums = [3, 5] => 출력 x  
#nums = [3, 3] => [0,1]
#nums = [1, 3, 4, 5, 2] => [0, 3] [2, 4] 둘 다 가능하지만 인덱스 값이 작은 것 이 출력됨
#nums = [1, 3, 4, 2] => [2 ,3]

target = 6
couple_nums = [] #뎃셈하여 타겟을 만들 수 있는 숫자 두개의 리스트

for i in range(target+1):
    couple_nums.extend([i, target-i])
    
        
    
    if i == target-i:
        if nums.count(i) == 2:
            index_num = [nums.index(i), nums.index(i, nums.index(i)+1)]
            print(index_num)
            break
        else:
            couple_nums= []
        continue               

    elif couple_nums[0] in nums and couple_nums[1] in nums:
   #Q- if couple_nums in num: 으로 하면 안되는 이유
        index_num = [nums.index(couple_nums[0]), nums.index(couple_nums[1])]
        print(index_num)
        break

    else:
        couple_nums= []
    continue
    #for문이 한번 돌아갈 때 마다 couple_num [0,9] > []   >[1,8] > []   >[2,7] > []   >[3,6] > []...[9,0]>[]