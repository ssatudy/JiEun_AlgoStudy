# blocks = [1, 0, 2, 3, 2, 0, 4]
blocks = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
h_block = max(blocks)

list(map(str, blocks))

new_blocks = []


water_blocks = 0

for f in range(max(blocks)+1): #f는 층수. 1층인 f=0 부터 시작해서 max 층인 f=max-1 까지
    for i in blocks:
        
        if i >= f+1:
            i = str(i)
            new_blocks.append(i.replace(i, '1'))
            continue
        else: 
            i = str(i)
            # i.replace(i, '0') 
            new_blocks.append(0)
            continue
    new_blocks = ''.join(map(str, new_blocks))
    new_blocks = new_blocks.strip('0')
    new_blocks = list(new_blocks)
    cnt = new_blocks.count('0')
    water_blocks += cnt
    new_blocks = []
    
print(water_blocks)
