#덧샘하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴.

nums= [3, 5]
target = 6
couple_nums = [] #뎃셈하여 타겟을 만들 수 있는 숫자 두개의 리스트

for i in range(target+1):
    couple_nums.extend([i, target-i])
    
    if couple_nums[0] in nums and couple_nums[1] in nums:
   #Q- if couple_nums in num: 으로 하면 안되는 이유
        index_num = [nums.index(couple_nums[0]), nums.index(couple_nums[1])]
        print(index_num)
        break
    
    else:
        couple_nums= []
    continue
    #for문이 한번 돌아갈 때 마다 couple_num [0,9] > []   >[1,8] > []   >[2,7] > []   >[3,6] > []...[9,0]>[]
