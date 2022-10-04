from collections import deque

n, m = map(int, input().split())
max_num = 100000
visited = [0]*(max_num +1)

def bfs():
    queue = deque()
    queue.append(n)

    while queue :
        x = queue.popleft()
        if x == m:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0<=j <=max_num and not visited[j]:
                visited[j] = visited[x]+1
                queue.append(j)
bfs()