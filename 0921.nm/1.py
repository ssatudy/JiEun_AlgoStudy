N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1, N + 1):
        if i not in ans:  # 중복 확인
            ans.append(i)
            back()    # 재귀
            ans.pop()    # return으로 돌아오면 이게 실행됨. 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것 / 마지막 재귀 끝나면 return돼서 한번 더 pop

back()

