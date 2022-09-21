N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def back():
    if len(ans) == M:
        print(*ans)
        return
    visited = []
    for i in range(N):
        if visited != lst[i]:
            ans.append(lst[i])
            visited = lst[i]
            back()
            ans.pop()

back()