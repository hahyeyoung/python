from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(N-1):
    a, b= list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        for i in tree[node]:
            if visited[i] ==0:
                visited[i]=node
                queue.append(i)
bfs()

for i in visited[2:]:
    print(i)


