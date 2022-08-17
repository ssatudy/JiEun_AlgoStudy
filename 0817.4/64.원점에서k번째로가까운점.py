n = 3    #좌표점의 개수
points = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
dis_list = []
for i in range(len(points)):
    dis = (points[i][0]**2 + points[i][1]**2)**1/2
    dis_list.append(dis)

sort_dis_list = sorted(dis_list)
k_dis = sort_dis_list[k-1]
index_k_dis = dis_list.index(k_dis)
result = points[index_k_dis]

print(result)