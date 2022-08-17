# 행의 개수 넣고, 열 값 넣어주기
# 5
# 1 4 7 11 15
# 2 5 8 12 19
# 3 6 9 16 22
# 10 13 14 17 24
# 18 21 23 26 30
# 5 or 20
r = int(input())
arr = [list(map(int, input().split())) for _ in range(r)]
target = int(input())
c = len(arr[0])
result = 0
for i in range(r):
    for j in range(c):
        if result == 'true':
            break
        if arr[i][j] == target:
            result = 'true'
            break
        else:
            result = 'flase'
print(result)
