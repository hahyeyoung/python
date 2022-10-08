import sys
from collections import deque
input = sys.stdin.readline

M,N,k = map(int, input().split())
graph = [[0]*N for _ in range(M)]

result = []
cnt = 1 #개수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y): #좌표에 따른 넓이 구하는 dfs
    global cnt
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    while queue:
        x, y =queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
                graph[nx][ny]=1
                queue.append([nx,ny])
                cnt +=1
    return cnt

for i in range(k):
    x, y, x1, y1 = map(int, input().split())
    for j in range(y,y1):
        for k in range(x,x1):
            graph[j][k] = 1

area = 0 #넓이
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            area +=1
            bfs(i,j)
            result.append(cnt)
            cnt = 1 #넓이 초기화
result.sort()
print(area)
print(' '.join(map(str,result)))