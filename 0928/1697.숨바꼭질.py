def back(r, c, ):
    global friends, cnt, d_rc
    if friends.count('Y') > 3:
        return
    if len(friends) == 7:
        if friends.count('S') >= 4:
            cnt += 1
        return

    for dd in range(4):
        R = r + dr[dd]
        C = c + dc[dd]
        if 0 <= R < 5 and 0 <= C < 5:
            if (R, C) not in d_rc:
                if d_rc:
                    if abs(d_rc[-1][0] - R) == 1 or abs(d_rc[-1][1] - C) == 1:
                        d_rc += [(R, C)]
                        friends.append(arr[R][C])
                        back(R, C)
                        friends.pop()
                        d_rc.pop()
                    else: return
                else:
                    d_rc += [(R, C)]
                    friends.append(arr[R][C])
                    back(R, C)


arr = list(input() for _ in range(5))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = []
cnt = 0
for i in range(5):
    for j in range(5):
        d_rc = []
        d_rc += [(i, j)]
        friends = [arr[i][j]]
        back(i, j)
print(cnt)