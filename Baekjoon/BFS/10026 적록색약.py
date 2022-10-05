from collections import deque

#BFS틀 만들기
def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    visited[x][y] == 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한경우
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] ==graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny])

N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))

visited = [[0]*N for _ in range(N)]
#적록색맹이 아닌경우
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt +=1

#적록색맹인 경우 : R을 G로 합치게 만듦
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] ='R'
cnt1 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 +=1
print(cnt, cnt1)