def back(k):
    global cur_sum, ret
    if cur_sum > m:
        return

    if k == 3 :
        cur_sum = sum(ans)
        if cur_sum > m:
            return
        ret.append(cur_sum)
        return

    for i in range(n):
        if lst[i] not in ans:
            ans.append(lst[i])

            back(k+1)
            ans.pop()
            cur_sum = 0



n, m = map(int, input().split())
lst = list(map(int, input().split()))
cur_sum = 0
ans = []
ret = []
back(0)
print(max(ret))
