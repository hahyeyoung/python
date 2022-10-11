#구술탈출 : 직사각형 보드에 빨간구슬, 파란구슬 => 빨간 구슬을 빼는것
# 세로 N, 가로 M, 바깥 행과 열은 막혀있음, 구멍하나
# 빨간구슬, 파란구슬 하나씩//빨간구슬이 구멍을 통해나옴, 파란구슬은 안됨
# 왼쪽으로 기울,오른쪽기울, 위쪽기울, 아래쪽 기울(네가지)
# 공은 동시에 움직임 : 파란구슬 실패, 동시에 빠져도 실패
# 동시에 같은 칸 불가능
# 최소 몇번만에 빨간 구슬을 통해 구멍을 나갈 수 있는지
# 10번 이하로 움직여서 빼낼 수 없으면 -1출력
# BFS 문제!
# .빈칸, #장애물, O구멍의 위치, .이동 가능, R빨간구슬, B파란구슬
from collections import deque
import sys
input = sys.stdin.readline # 빠른 입출력 위한 코드

#입력창
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input().strip()))
    for j in range(M):
        if graph[i][j] =='R': #빨간 구슬 위치
            rx, ry = i,j
        elif graph[i][j] =='B': #파란 구슬 위치
            bx, by = i,j
#왼오른위아래
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(rx,ry,bx,by):
    queue=deque()
    queue.append((rx,ry,bx,by))
    visited = [] #방문여부리스트
    visited.append((rx,ry,bx,by))
    count = 0
    while queue:
        for _ in range(len(queue)):
            rx,ry,bx,by = queue.popleft()
            if count > 10 : #움직인 횟수가 10회 초과면 -1출력
                print(-1)
                return
            if graph[rx][ry] == 'O': #현재 빨간 구슬의 위치가 구멍
                print(count)
                return
            #4방향 탐색
            for i in range(4):
                #빨간구슬 구하기 방향이동
                nrx, nry = rx, ry
                while True:
                    nrx+=dx[i]
                    nry+=dy[i]
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == 'O':
                        break
                #파란구슬 방향이동
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break
                if graph[nbx][nby] =='O': #파란구슬먼저
                    continue
                if nrx == nbx and nry == nby: #두 구슬의 위치가 같음
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):  # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:  # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count +=1
    print(-1)
bfs(rx,ry,bx,by)
