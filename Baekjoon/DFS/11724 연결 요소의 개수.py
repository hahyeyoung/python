import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[ ]*M for i in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,visited,v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            dfs(graph,visited,i)

for i in range(1,N+1):
    if visited[i]==0:
        if graph[i]==0:
            cnt +=1
            visited[i] =1
        else:
            dfs(graph, visited,i)
            cnt+=1
print(cnt)



