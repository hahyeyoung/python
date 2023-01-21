
N,M = map(int,input().split())
board = []
result = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        test1 = 0
        test2 = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0 :
                    if board[a][b] != 'B':
                        test1 +=1
                    if board[a][b] != 'W':
                        test2 +=1
                else :
                    if board[a][b] != 'W':
                        test1 +=1
                    if board[a][b] != 'B':
                        test2 +=1
        result.append(test1)
        result.append(test2)

print(min(result))