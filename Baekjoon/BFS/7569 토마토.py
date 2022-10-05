from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0 ,0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0<=z<h and graph[z][x][y] == 0:
                queue.append([nx, ny, nz])
                graph[nz][nx][ny] = graph[z][x][y] + 1
m, n, h = map(int, input().split())
graph = [[] for i in range(h)]
queue = deque([])
for i in range(h):
    for j in range(n):
        graph.append(list(map(int, input().split())))

for z in range(h):  # 익은 토마토 큐에 저장
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
            queue.append([x,y,z])
bfs()
result = 0
for z in range(h):  # 익은 토마토 큐에 저장
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                      print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)

