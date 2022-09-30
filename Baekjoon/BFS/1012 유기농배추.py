import sys
from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for a in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    graph = [[0]*n for i in range(m)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt +=1
    print(cnt)