from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

count = []
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))

    graph[x][y] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n :
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt +=1
    count.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)

count.sort()

print(len(count))

for i in count:
    print(i)