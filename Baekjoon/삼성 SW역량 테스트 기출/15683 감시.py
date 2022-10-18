import copy

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

#상하좌우
dx = [-1,0,1,0]
dy = [0,1,0,-1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(x,y, direction, temp):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx<0 or nx>=n or ny<0 or ny>=m or temp[nx][ny]==6:
                break
            elif temp[nx][ny]==0:
                temp[nx][ny]='#'
def dfs(n, matrix):
    global result
    temp = copy.deepcopy(matrix)

    if n == len(cctv):
        count =0
        for t in temp:
            count += t.count(0)
        result = min(result, count)
        return
    x, y, c = cctv[n]
    for d in direction[c]:
        watch(x,y,d,temp)
        dfs(n+1, temp)
        temp = copy.deepcopy(matrix)

cctv = []
result = 1e9

for i in range(n):
    for j in range(m):
        if matrix[i][j] !=0 and matrix[i][j] !=6:
            cctv.append([i,j,matrix[i][j]])
dfs(0,matrix)
print(result)