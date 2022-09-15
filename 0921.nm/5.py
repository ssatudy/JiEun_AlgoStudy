N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(N):
        if lst[i] not in ans:
            ans.append(lst[i])
            back()
            ans.pop()

back()