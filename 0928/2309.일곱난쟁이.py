
def back(idx, cur_sum, k):
    global ret
    if k == 7:
        if sum(cur_sum) == 100:
            ret = cur_sum
            return ret
    for i in range(idx, 9):
        if sum(cur_sum) <= 100:
            back(i+1, cur_sum + [lst[i]], k + 1)
        else:
            return


lst = sorted([int(input()) for _ in range(9)])
ret = []
back(0, [], 0)
for n in ret:
    print(n)