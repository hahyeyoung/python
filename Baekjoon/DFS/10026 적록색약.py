import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y]=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny]==graph[x][y] and not visited[nx][ny]:
            dfs(nx,ny)

N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))
visited = [[0]*N for _ in range(N)]
cnt = 0
# 적록색맹이 아닌경우
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            cnt+=1
#적록색맹인 경우
cnt1 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            graph[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            cnt1+=1

print(cnt, cnt1)