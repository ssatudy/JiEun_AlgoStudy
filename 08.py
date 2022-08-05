# blocks = [1, 0, 2, 3, 2, 0, 4]
blocks = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

h_block = max(blocks) # 최고층의값, 바깥 for문이 시행될 횟수를 정한다

list(map(str, blocks)) # if문에서 .replace() 사용을 해야돼서 int를 str로 변환

new_blocks = [] #층수 별로 1, 0 값을 넣을 리스트

water_blocks = 0 #물 블럭의 개수

#
for f in range(max(blocks)+1): #f는 층수. 1층인 f=0 부터 시작해서 max 층인 f=max-1 까지 
    for i in blocks:
        
        if i >= f+1: #i가 층수와 같거나 층수보다 큰 값을 가질 때 i = 1
            i = str(i)
            new_blocks.append(i.replace(i, '1'))
            continue
        else: #i 가 층수보다 작은 값을 가질 떄 i = 0
            i = str(i)
            new_blocks.append(0)
            continue

    new_blocks = ''.join(map(str, new_blocks)) # .strip()함수를 사용해야 돼서 list > str

    new_blocks = new_blocks.strip('0') # 양쪽 끝에 0 제거
    new_blocks = list(new_blocks) # 0의 개수를 count 해야돼서 str > list
    cnt = new_blocks.count('0') # 0의 개수 = 물 블럭의 개수.
    water_blocks += cnt
    new_blocks = []
    
print(water_blocks)
