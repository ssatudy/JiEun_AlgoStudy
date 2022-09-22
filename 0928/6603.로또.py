def back(k):
    global used
    if k == 6:
        print(*ans)

        return
    for i in range(l):
        if lst[i] not in ans:
            ans.append(lst[i])
            back(k+1)
            ans.pop()



lst = list(map(int, input().split()))
k = lst[0]
lst = lst[1:len(lst)]
l = len(lst)
visited = []
used = []
ans = []
back(0)
