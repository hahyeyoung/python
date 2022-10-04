from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue :
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            cnt +=1
            visited[i] = 1
        else :
            bfs(i)
            cnt +=1
print(cnt)
