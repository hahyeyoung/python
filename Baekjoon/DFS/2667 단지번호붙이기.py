
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(graph, v):
    graph[v] = 0
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(graph,i)
            cnt += 1

