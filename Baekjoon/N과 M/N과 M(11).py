import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
result = []


def dfs():
    if len(result) == M:
        print(*result)
        return
    temp = 0
    for i in range(N):
        if temp!=num[i]:
            result.append(num[i])
            temp = num[i]
            dfs()
            result.pop()
dfs()
