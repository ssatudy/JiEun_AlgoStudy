n = 5   #조합 할 숫자의 개수
nums = [list(map(int, input())) for _ in range(n)] #21 85 88 21 22
nums = sorted(nums)     # [[2, 1], [2, 1], [2, 2], [8, 5], [8, 8]]
n_num = []
max_nums = []
for i in range(n):     # [[8, 8], [8, 5], [2, 2], [2, 1], [2, 1]]
    n_num.append(nums[-1-i])
    for j in range(len(n_num[i])):
        max_nums.append(n_num[i][j])
print(''.join(map(str, max_nums)))
