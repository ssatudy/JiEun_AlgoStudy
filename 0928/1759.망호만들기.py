from sys import stdin
<<<<<<< HEAD
=======
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
>>>>>>> cfdb120ae02896fc491fa05d7996c3cda6d814a5

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
<<<<<<< HEAD
lst = list(stdin.readline().split())
lst = sorted(lst)
vol = ['a', 'e', 'i', 'o', 'u']
used = {}
visited = [0]*n
back(0, '', 0)
=======
lst = sorted(list(stdin.readline().split()))

ans = []
visited = [0]*n
used = {}
back(0, [])
>>>>>>> cfdb120ae02896fc491fa05d7996c3cda6d814a5
