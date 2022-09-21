from itertools import combinations
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = sorted(set(combinations(lst, m)))

for i in ans:
    for j in i:
        print(j, end=" ")
    print()



