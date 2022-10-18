
#가로선 확인
def check():
    for start in range(N):
        k=start
        for line in range(H):
            if board[line][k]:
                k+=1
            elif k>0 and board[line][k-1]:
                k-=1
        if k!=start :
            return False
    return True

def dfs(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return
    elif cnt ==3 or result <= cnt:
        return
    for i in range(x,H):
        if i==x:
            k = y
        else :
            k = 0
        for j in range(k,N-1):
            if not board[i][j] and not board[i][j+1]:
                if j>0 and board[i][j-1]:
                    continue
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j]=0

N,M,H = map(int, input().split())
board = [[0]* N for _ in range(H)]
if M == 0:
    print(0)
    exit(0)
for i in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
result = 4
dfs(0,0,0)
if result < 4:
    print(result)
else :
    print(-1)