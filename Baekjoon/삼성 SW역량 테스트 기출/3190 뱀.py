#뱀이 나와서 기어다니는데, 사과를 먹으면 뱀길이가 늘어남
# 벽 또는 자기자신의 몸과 부딪히면 게임끝
# N*N 정사각 보드위에서 진행, 몇몇 칸에는 사과가 놓여져 있음
# 보드의 상하좌우 끝에 벽이 있음
#뱀은 맨위 맨좌측 위치, 뱀의 길이는 1
#뱀은 처음에 오른쪽으로 향함
#뱀은 매 초마다 이동
# 뱀은 몸길이를 늘려 다음칸에 위치
# 이동 칸에 사과가 있으면, 사과는 없어지고 꼬리는 움직이지 않음
# 사과가 없으면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌, 몸길이는 변하지 않음
# 게임이 몇초에 끝나는지 계산
from collections import deque

def dir_change(d,c): #d는 방향, c는 원소
    if c == 'L':
        d = (d-1)%4
    elif c== 'D':
        d = (d+1)%4
    return d
#상, 우 , 하, 좌
# 동쪽회전(오른쪽회전) : 상-우-하-좌 : +1
# 서쪽회전(왼쪽회전) : 상-좌-하-우 : -1
dy= [-1,0, 1, 0]
dx= [0, 1, 0,-1]

def start():
    direction = 1 #초기방향
    time = 1
    y,x = 0,0 #초기뱀 위치
    snake = deque([[y,x]]) #방문위치
    matrix[y][x] =1 #뱀이 지나간 자리, 현재위치

    while True:
        y,x = y+dy[direction], x+dx[direction]
        if 0<= y<N and 0<=x<N and matrix[y][x] !=1:
            #사과가 없는 경우
            if not matrix[y][x] == 2:
                ny, nx = snake.popleft()
                matrix[ny][nx] = 0
            matrix[y][x] = 1
            snake.append([y,x])
            if time in times.keys():
                direction = dir_change(direction, times[time])
            time+=1
        else: #본인 몸에 부딧히커나 벽에 부딪힌 경우
            return time


N = int(input()) #보드의 크기
K = int(input()) #사과의 개수

matrix = [[0]*N for _ in range(N)]

#사과의 위치 넣기
for i in range(K):
    a,b = map(int, input().split())
    matrix[a-1][b-1] = 2 #사과 있음
times = {}
L = int(input())#뱀의 방향 변환 횟수
for i in range(L):
    X,C = input().split()
    times[int(X)] = C
print(start())
