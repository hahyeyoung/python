n,m = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int,input().split())
B = [list(map(int, input().split())) for _ in range(m)]

C = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            C[i][j] += A[i][x] * B[x][j]

for i in C:
    for j in i:
        print(j, end=' ')
    print()