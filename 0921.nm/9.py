from itertools import permutations
n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = sorted(set(permutations(lst, m)))

for i in ans:
    for j in i:
        print(j, end=" ")
    print()