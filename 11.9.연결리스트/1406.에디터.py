word = list(input())
cursor_idx = len(word)

for _ in range(int(input())):
    C = input()
    move = C[0]
    if len(C) == 3:
        add_word = C.pop()
    if move == 'L' and cursor_idx > 0:
        cursor_idx -= 1
    elif move == 'D' and cursor_idx < len(word):
        cursor_idx += 1
    elif move == 'B' and cursor_idx > 0:
        word.pop(cursor_idx-1)
        cursor_idx -= 1
    elif move == 'P':
        word.insert(cursor_idx, add_word)
        cursor_idx += 1

print(''.join(word))