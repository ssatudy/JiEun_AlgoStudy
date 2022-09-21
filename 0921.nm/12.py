from itertools import combinations_with_replacement
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = sorted(set(combinations_with_replacement(lst, m)))

for i in ans:
    for j in i:
        print(j, end=" ")
    print()