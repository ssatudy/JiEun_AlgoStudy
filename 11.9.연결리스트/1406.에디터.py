
word = list(input())
cursor_idx = len(word)
word_right = []

for _ in range(int(input())):
    C = input()
    move = C[0]
    if move == 'L' and cursor_idx > 0:
        word_right.append(word.pop())
        cursor_idx -= 1
    elif move == 'D' and cursor_idx < len(word):
        word.append(word_right.pop())
        cursor_idx += 1
    elif move == 'B' and cursor_idx > 0:
        word.pop()
        cursor_idx -= 1
    elif move == 'P':
        word.append(C[2])
        cursor_idx += 1

word_right = reversed(word_right)
word.extend(word_right)
print(''.join(word))