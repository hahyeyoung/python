def solution(n, results):
    graph = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        graph[win - 1][lose - 1] = True
        graph[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] == None:
                    continue

                if graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = not graph[j][i]

    answer = 0
    for i in range(n):
        if None in graph[i][:i] + graph[i][i + 1:]:
            continue
        answer += 1
    return answer