def back(r, c, ):
    global friends, cnt
    if friends.count('Y') > 3:
        return
    if len(friends) == 7 :
        if friends.count('S') >= 4:
            cnt += 1
        return
    for dd in range(4):
        R = r + dr[dd]
        C = c + dc[dd]
        if 0 <= R < 5 and 0 <= C < 5:

            if (R, C) not in d_rc:
                d_rc[(R, C)] = 1
                friends.append(arr[R][C])
                back(R, C)
                del d_rc[(R, C)]
                friends.pop()



arr = list(input() for _ in range(5))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cnt = 0
for i in range(5):
    for j in range(5):
        d_rc = {}
        d_rc[(i, j)] = 1
        friends = [arr[i][j]]
        back(i, j)
print(cnt)