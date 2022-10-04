import sys
from collections import deque
from itertools import combinations
import copy

#입력값 속도 줄이기
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [] #그래프
blank = [] #벽
virus = [] #바이러스
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v, copy_graph):
    visited = [[0]*m for _ in range(n)]
    for k in v:
        qeueu = deque()
        qeueu.append((k[0], k[1]))
        visited[k[0]][k[1]] = True
        while qeueu:
            x, y = qeueu.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if copy_graph[nx][ny] == 1:
                        visited[nx][ny] = 1
                        continue
                    elif graph[nx][ny] == 0:
                        if visited[nx][ny] == 0:
                            copy_graph[nx][ny] = 2
                            visited[nx][ny] = 1
                            qeueu.append((nx, ny))
    count = 0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                count += 1
    return count

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 0:
            blank.append([i, j])
        elif data[j] == 2:
            virus.append([i, j])
    graph.append(data)

max_count = 0
for combi in list(combinations(blank, 3)):
    copy_graph = copy.deepcopy(graph)
    for c in combi:
        x, y = c
        copy_graph[x][y] = 1
    count = bfs(virus, copy_graph)
    max_count = max(max_count, count)

print(max_count)

''' 1) 시간초과
n,m = map(int, input().split())
graph = [] #초기맵
matrix = [[0]*m for _ in range(n)] #벽을 설치한 뒤의 맵 리스트
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

#바이러스가 퍼지는 것
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                virus(nx,ny)
#안전 영역 계산
def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                score +=1
    return score

def dfs(count):
    global result
    if count == 3: # 벽이 3개가 설치되었을 때 바이러스 전파
        for i in range(n):
            for j in range(m):
                matrix[i][j] = graph[i][j]
        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 2:
                    virus(i,j)
        result = max(result, score())
        return
    #빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count +=1
                dfs(count)
                graph[i][j] = 0
                count -= 1
dfs(0)
print(result)
'''

