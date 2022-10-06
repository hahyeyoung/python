from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0 ,0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0<= nz< h:
                if graph[nz][nx][ny]== 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append([nz, nx, ny])



m, n, h = map(int, input().split())
graph = [[list(map(int,input().split())) for i in range(n)]for i in range(h)]
queue = deque([])

for z in range(h):  # 익은 토마토 큐에 저장
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append([z,x,y])
bfs()
z = 1
result = -1
for i in graph:  # 익은 토마토 큐에 저장
    for j in i:
        for k in j:
            if k == 0:
                z = 0

            result = max(result, k)
if z == 0: #모두 익히지 못한 상태
    print(-1)
elif result == 1:  #모두 익었던 상태
    print(0)
else :
    print(result-1)
