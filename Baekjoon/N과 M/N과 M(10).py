import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
visited = [False] * N
result = []


def dfs(start):
    if len(result) == M:
        print(*result)
        return
    temp = 0
    for i in range(start,N):
        if not visited[i] and temp!=num[i]:
            result.append(num[i])
            visited[i] = True
            temp = num[i]
            dfs(i)
            result.pop()
            visited[i] = False
dfs(0)