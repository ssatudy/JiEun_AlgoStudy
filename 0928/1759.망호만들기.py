from sys import stdin
def back(k, ans):
    ret = sorted(ans)
    ret = ''.join(ret)
    if k == m and ret not in used and (ans.count('a') + ans.count('e') + ans.count('i') + ans.count('o') + ans.count('u')) >= 1:
        used[ret] = 1
        print(ret)
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            back(k+1, ans + [lst[i]])
            visited[i] = 0


m, n = map(int, stdin.readline().split())
lst = sorted(list(stdin.readline().split()))

ans = []
visited = [0]*n
used = {}
back(0, [])
