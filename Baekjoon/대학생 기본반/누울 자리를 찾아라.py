import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

hor = 0 #가로
ver = 0 #세로

for i in range(n):
    temp1, temp2 = 0, 0
    for j in range(n):
        if graph[i][j] == '.':
            temp1 +=1
        else :
            temp1 = 0

        if temp1 ==2 :
            hor +=1

        if graph[j][i] == '.':
            temp2 += 1
        else:
            temp2 = 0
        if temp2 == 2:
            ver += 1

print(hor,ver)