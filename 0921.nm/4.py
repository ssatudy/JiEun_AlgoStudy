n, m = map(int, input().split())
ans = []
def back():
    if m == len(ans):
        print(*ans)
        return

    for i in range(1, n+1):
        if not ans:
            ans.append(i)
            back()
            ans.pop()
        elif i >= ans[-1]:
            ans.append(i)
            back()
            ans.pop()

back()