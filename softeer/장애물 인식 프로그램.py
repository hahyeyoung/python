from collections import deque
n = int(input())
graph = []
block = []
for i in range(n):
    graph.append(list(map(int,input().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y]=0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt +=1
    block.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)

print(len(block))

block.sort()
for k in block:
    print(k)