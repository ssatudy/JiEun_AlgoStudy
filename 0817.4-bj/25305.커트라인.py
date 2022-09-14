import sys
n, k = map(int, sys.stdin.readline().split())
score = map(int, sys.stdin.readline().split())
score = sorted(score)
print(score[-k])