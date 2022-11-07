N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
res = []
L = len(arr)
idx = K - 1
res.append(arr.pop(idx))

while arr:
    idx = (idx+K) % L
    res.append(arr.pop(idx))
    L = len(arr)
