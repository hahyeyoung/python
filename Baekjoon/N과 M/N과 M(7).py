import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
result = []


def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        result.append(num[i])
        dfs()
        result.pop()
dfs()
