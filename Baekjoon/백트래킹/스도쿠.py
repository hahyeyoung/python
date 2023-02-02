graph = []
temp = []
for i in range(9):
    graph.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0 :
            temp.append((i,j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(temp):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = temp[idx][0]
        y = temp[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)
