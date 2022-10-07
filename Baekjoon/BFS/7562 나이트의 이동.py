from collections import deque

#나이트가 한번에 이동할 수 있는 칸
#대각선 2칸씩!!
#테스트 케이스 수 ,체스판 한변의 길이, 나이트가 현재 있는 칸, 이동하려고 하는 칸

#대각선 2칸씩 8방향
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x,y,x1,y1):
    queue = deque()
    queue.append([x,y])
    matrix[x][y]=1
    while queue:
        x,y = queue.popleft()
        if x== x1 and y==y1 :
            return matrix[x][y]-1
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and matrix[nx][ny]==0:
                matrix[nx][ny] = matrix[x][y]+1
                queue.append([nx,ny])


T = int(input())
for i in range(T):
    l = int(input()) # 체스판 한변의 길이
    matrix = [[0]*l for _ in range(l)]
    x1,y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    result = bfs(x1,y1,x2,y2)
    print(result)





