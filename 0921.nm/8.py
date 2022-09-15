N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def back():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):

        if not ans:
            ans.append(lst[i])
            back()
            ans.pop()
        elif ans[-1] <= lst[i]:
            ans.append(lst[i])
            back()
            ans.pop()
back()