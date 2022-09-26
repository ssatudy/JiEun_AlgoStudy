def back(arr):
    global visited, ans
    if len(ans) == 6:
        print(*ans)
    for i in range(l):
        if ans:
            if i not in visited and lst[i] > ans[-1]:
                visited.append(i)
                ans.append(lst[i])
                back(lst)
                ans.pop()
                visited.pop()
        else:
            if i not in visited:
                visited.append(i)
                ans.append(lst[i])
                back(lst)
                ans.pop()
                visited.pop()

p = 0
while p == 0:
    lst = list(map(int, input().split()))
    if len(lst) == 1: break
    else:
        n = lst[0]
        lst.pop(0)
        l = len(lst)
        visited = []
        ans = []
        back(lst)
        print()