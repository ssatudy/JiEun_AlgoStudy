from sys import stdin
def back(k):
    ret = sorted(ans)
    ret = ''.join(ret)
    if k == m and ret not in used:
        used[ret] = 1
        print(ret)
        return
    for i in range(n):
        if i not in visited:
            visited.append(i)
            ans.append(lst[i])
            back(k+1)
            ans.pop()
            visited.pop()


m, n = map(int, stdin.readline().split())
lst = sorted(list(stdin.readline().split()))

ans = []
visited = []
used = {}
back(0)
