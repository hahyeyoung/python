from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited[1] = 1
    q = deque([1])

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    max_v = max(visited)
    answer = visited.count(max_v)

    if answer > 0:
        return answer
    else:
        return 1