n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    if graph[x][y] == 1:
        cnt +=1
        graph[x][y] = 0
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0
result.sort()

print(len(result))
for k in result:
    print(k)
