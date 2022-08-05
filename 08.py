'''
blocks = [0,1,0,2,1,0,1,3,2,1,2,1]

total_volume = []

for i in range(len(blocks)-1):
    k = abs(blocks[i-1] - blocks[i+1]) - blocks[i]
    if k > 0:
        total_volume.append(k)

print(sum(total_volume))
'''

'''
1.
blocks을 돌며 값이 1이상인 경우 1로 바꾸고 0 이면 0 
1사이에 있는 0의 개수를 물 블럭에 추가

2.
blocks을 돌며 2 이상인 값들은 1로 1이나 0은 0으로
1과 1사이에 있는 0의 값 출력 
'''

