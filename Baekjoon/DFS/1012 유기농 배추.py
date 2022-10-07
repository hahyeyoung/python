#재귀 리미트 설정
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <m and 0<= ny <n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx,ny)

t = int(input())

for i in range(t) :
    m, n, k = map(int, input().split())
    graph = [[0]*n for i in range(m)]
    for i in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i,j)
                result+=1
    print(result)
