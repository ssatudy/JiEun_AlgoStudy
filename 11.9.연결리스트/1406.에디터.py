import sys
word = list(sys.stdin.readline().strip())
word_right = []
N = int(input())

for _ in range(N):
    C = sys.stdin.readline().split()

    if C[0] == 'L' and word:
        word_right.append(word.pop())

    elif C[0] == 'D' and word_right:
        word.append(word_right.pop())

    elif C[0] == 'B' and word:
        word.pop()

    elif C[0] == 'P':
        word.append(C[1])


word_right = list(reversed(word_right))
print(''.join(word + word_right))