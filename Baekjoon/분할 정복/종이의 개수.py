n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

result1 = 0
result2 = 0
result3 = 0

def dfs(x,y,n):
    global result1,result2,result3
    check = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != check :
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
    if check == -1 :
        result1 +=1
    elif check == 0 :
        result2 +=1
    else :
        result3 +=1

dfs(0,0,n)
print(result1)
print(result2)
print(result3)