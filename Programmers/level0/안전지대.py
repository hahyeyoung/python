def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    #지뢰가 설치된 곳
    graph = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                graph.append((x, y))

    #지뢰가 설치된 곳 주변에 폭탄 설치
    for x, y in graph:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1

    #폭탄이 설치되지 않은 곳만 카운팅
    answer = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                answer += 1

    return answer