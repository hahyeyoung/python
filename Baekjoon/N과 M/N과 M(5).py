import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
visited = [False] * N
result = []


def dfs(depth):
    if depth == M:
        print(' '.join(map(str, result)))
    for i in range(N):
        if not visited[i]:
            result.append(num[i])
            visited[i] = True
            dfs(depth + 1)
            result.pop()
            visited[i] = False


dfs(0)
