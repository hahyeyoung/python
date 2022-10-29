from collections import deque

x,y = map(int, input().split())

graph = [[0]*(y-1) for _ in range(x-1)]

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    graph[a][b] = 1
    while queue:
        a, b = queue.popleft()
        dx = a+1
        dy = b+1
        if graph[dx][dy]== 1 and 0<dx<=x-1 and 0<dy<=y-1:
            graph[dx][dy] = 1
            queue.append([dx,dy])
        elif dx>x-1 or dy>y-1 :
            dx = (a+1)%a
            dy = (b+1)%b
            graph[dx][dy] = 1
            queue.append([dx, dy])
if x<=2 and y<=2:
    print(-1)
else:
    bfs(0,0)
for i in range(x-1):
    for j in range(y-1):
        if graph[i][j] == 0 :
            print('false')
            break
print('True')
