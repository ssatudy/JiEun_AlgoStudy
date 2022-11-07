N = int(input())
for _ in range(N):
    input_key = list(input())
    password1, password2 = [], []

    for k in input_key:
        if k == '<':
            if password1:
                password2.append(password1.pop())
        elif k == '>':
            if password2:
                password1.append(password2.pop())
        elif k == '-':
            if password1:
                password1.pop()
        else:
            password1.append(k)
    print(''.join(password1+list(reversed(password2))))
