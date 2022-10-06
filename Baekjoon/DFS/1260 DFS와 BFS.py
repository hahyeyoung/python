from collections import deque


def BFS(v, Matrix, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for w in Matrix[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True


def DFS(v, List, Check):
    Check[v] = True
    print(v, end=' ')
    for i in List[v]:
        if not Check[i]:
            DFS(i, List, Check)


N, M, V = map(int, input().split())

Matrix = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    Matrix[u].append(v)
    Matrix[v].append(u)
    for i in range(len(Matrix)):
        Matrix[i].sort()
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)
DFS(V, Matrix, visited1)
print()
BFS(V, Matrix, visited2)