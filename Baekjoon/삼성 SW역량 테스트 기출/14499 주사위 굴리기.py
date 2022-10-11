# N*M 지도 존재
# 오른쪽은 동쪽, 위쪽은 북쪽
# 지도의 좌표(r,c), r은 북쪽으로 떨어진 칸의 개수, c는 서쪽으로 떨어진 칸의 개수
#지도위 윗 면이 1, 동쪽을 바라보는 방향 3, 좌표는(x,y)
# 주사위 모든 면에 0이 적혀있음
#지도의 각 칸에는 정수가 하나씩 쓰여있음
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,주사위 바닥면에 쓰여 있는 수가 칸에 복사
# 0이 아닌 경우 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여 있는 수는 0
# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다, 상단에 쓰여 있는 값을 구하시오
# 주사위는 지도의 바깥으로 이동불가, 이동하는 경우 명령 무시

# 주사위를 놓고, 주사위를 상,하,좌,우로 굴림, 바닥에 닿는 면은 맵의 숫자로 복사가 됨
# 주사위를 굴렸을 때 주사위 위쪽면의 숫자 출력

#입력값
N, M, x, y, k = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int,input().split())))
move_dir = list(map(int, input().split()))

#원본주사위 : 위, 아래, 왼, 오, 앞, 뒤
dice = [0,0,0,0,0,0]

def dice_move(i):
    if i == 1 : #동쪽
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif i == 2: #서쪽
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif i == 3: #북쪽
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif i == 4: #남쪽
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

#동서북남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in move_dir:
    nx = x+dx[i-1] #1을 빼주는 이유는 방향이 4방향으로 넣어 있어서
    ny = y+dy[i-1]
    if 0<= nx< N and 0<= ny < M :
        dice_move(i)
        if matrix[nx][ny]==0:
            matrix[nx][ny]=dice[1]
        else:
            dice[1] = matrix[nx][ny]
            matrix[nx][ny] = 0
        x = nx
        y = ny
        print(dice[0])
    else :
        continue
