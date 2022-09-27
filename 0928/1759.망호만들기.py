from sys import stdin

def back(k, ans, idx):
    if k == m and ans not in used:
        cnt = 0
        used[ans] = 1
        for j in range(m):
            if ans[j] in vol:
                cnt += 1
        if 1 <= cnt <= m - 2:
            print(ans)
            return

    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            back(k+1, ans + lst[i], i + 1)
            visited[i] = 0

m, n = map(int, stdin.readline().split())
lst = list(stdin.readline().split())
lst = sorted(lst)
vol = ['a', 'e', 'i', 'o', 'u']
used = {}
visited = [0]*n
back(0, '', 0)
