from collections import deque

# 노드의 간선 및 개수 받기
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, v):
    global cnt
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    print(cnt)

bfs(graph, 1)
