from collections import deque

#N*M행렬 맵/ 0은 이동가능, 1은 이동불가
#(1,1)->(N,M) 최단경로
#시작하는 칸과 끝나는 칸 포함
#상하좌우, 벽을 한개는 부수기 가능

N,M = map(int, input().split())
graph = []
visited = [[[0]*2 for _ in range(M)]for _ in range(N)]
visited[0][0][0]=1
for i in range(N):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))
    while queue:
        x, y, z = queue.popleft()
        #끝점에 도달하면 이동 횟수 출력
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            #이동할 곳이 벽이고, 벽파괴 기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and z==0:
                visited[nx][ny][1] = visited[x][y][0]+1
                queue.append((nx,ny,1))
            #이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은경우:
            elif graph[nx][ny]==0 and visited[nx][ny][z]==0:
                visited[nx][ny][z] = visited[x][y][z]+1
                queue.append((nx,ny,z))
    return -1

print(bfs(0,0,0))



