import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
result = []


def dfs(start):
    if len(result) == M:
        print(*result)
        return
    for i in range(start,N):
        result.append(num[i])
        dfs(i)
        result.pop()
dfs(0)
