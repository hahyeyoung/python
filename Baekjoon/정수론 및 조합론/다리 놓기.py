import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
    for i in range(1,a+1):
        for j in range(1, b+1):
            if i==1:
                dp[i][j] = j
                continue
            if i==j:
                dp[i][j] = 1
            else :
                if j>i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[a][b])