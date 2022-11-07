def back(k, cur_sum, idx):
    global ret
    if k == 11:
        ret = max(cur_sum , ret)
        cur_sum = 0
        return

    for j in range(11):
        if arr[idx][j] != 0:
            if j not in d:
                d[j] = 1
                back(k+1, cur_sum + arr[idx][j], idx + 1)
                del d[j]

for tc in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(11)]
    lst = [[] for _ in range(11)]
    d = {}
    ret = 0

    back(0, 0, 0)
    print(ret)