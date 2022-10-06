n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,visited, v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            dfs(graph,visited, i)
            cnt += 1

dfs(graph,visited, 1)
print(cnt)