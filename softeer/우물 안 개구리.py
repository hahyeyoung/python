import sys
N, M = map(int,input().split())
weight = list(map(int,input().split()))
best = [1]*(N)

for j in range(M):
    a, b =map(int, input().split())
    if weight[a-1] > weight[b-1]:
        best[b-1] = 0
    elif weight[a-1] < weight[b-1]:
        best[a-1] = 0
    else :
        best[a-1] = 0
        best[b-1] = 0
print(sum(best))