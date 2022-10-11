#로봇 청소기가 주어졌을 때, 청소하는 영역의 개수
# N*M직사각형
# 각각의 칸은 벽또는 빈칸
# 청소기는 바라보는 방향이 있음
# 동서남북중 하나
# 현재위치 청소
#현재위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색 진행
N,M = map(int, input().split())
x,y,d = map(int, input().split())
matrix = []
visited = [[0]*M for _ in range(N)]
for i in range(N):
    matrix.append(list(map(int, input().split())))
#범위설정 : 북동남서: 0,1,2,3
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#회전방향 : 서->남->동->북

visited[x][y] =1
cnt =1

while True :
    back = 0
    for i in range(4):
        nx = x+dx[(d+3)%4]
        ny = y+dy[(d+3) % 4]
        d = (d +3) % 4  # 방향바꾸기
        if visited[nx][ny]==0 and matrix[nx][ny]==0:
            x, y =nx,ny
            visited[nx][ny] = 1 #값 1로 변경
            cnt +=1
            back +=1
            break
    if back == 0: #4방향 청소가 다 되었을 경우
        if matrix[x-dx[d]][y-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            x,y = x-dx[d],y-dy[d]




