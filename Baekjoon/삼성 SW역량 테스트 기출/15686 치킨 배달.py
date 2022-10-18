from itertools import combinations
N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

ch = []
home = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append([i, j])
        #    home.append([i+1,j+1])
        elif graph[i][j] == 2:
            ch.append([i, j])
        #    ch.append([i + 1,j + 1])

        else :
            continue
result = 1e9
##치킨거리 구하기
for chi in combinations(ch, M):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in home:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)
print(result)
