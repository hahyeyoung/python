import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(N-1):
    a, b= list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    for i in tree[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)
dfs(1)
for i in range(2,N+1):
    print(visited[i])
