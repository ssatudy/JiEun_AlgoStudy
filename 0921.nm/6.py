N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(N):
        if not ans:
            ans.append(lst[i])
            back()
            ans.pop()
        elif lst[i] not in ans and lst[i] > ans[-1]:
            ans.append(lst[i])
            back()
            ans.pop()

back()
