#눈금 간격 1 N*M크기의 모눈종이
#모눈종이 위에 눈금에 맞추어 K개의 직사각형 그림
#K개의 직사각형의 내부를 제외한 나머지 부분이 분리됨
#분리된 부분의 넓이 구하기

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

M,N,k = map(int, input().split())
graph = [[0]*N for _ in range(M)]

result = []
cnt = 1 #개수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x,y): #좌표에 따른 넓이 구하는 dfs
    global cnt
    graph[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
            dfs(nx,ny)
            cnt +=1

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
            dfs(i,j)
            result.append(cnt)
            cnt = 1 #넓이 초기화
result.sort()
print(area)
print(' '.join(map(str,result)))
