# 4*4보드의 혼자 즐기는 게임
# 한번의 이동은 보드 위에 있는 전체 블록 상하좌우
# 같은 값을 같는 블록이 충돌하면 합쳐짐
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
from copy import deepcopy

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
result = 0


#왼쪽방향
def left(board) :
    for i in range(N) :
        p = 0 # 열의 가장 좌측
        x = 0
        for j in range(N) :
            if board[i][j] == 0 : # 빈칸이면 continue
                continue
            if x == 0 : # x가 비어있으면 더해줄 이전 블록이 없다는 의미이므로, x를 변경
                x = board[i][j]
            else :
                if x == board[i][j] : # 블록의 숫자가 같다면
                    board[i][p] = x * 2
                    x = 0 # 블록을 더했으므로 0으로 다시 초기화
                    p += 1 # 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하기 위한 위치 증가
                else :
                    board[i][p] = x # 이동할 곳에 지난 블록 x를 저장
                    x = board[i][j] # 이전 블록을 새로운 블록으로 변경
                    p += 1 # 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하기 위한 위치 증가
            board[i][j] = 0 # 블록 이동했으므로 비워줌
        if x != 0 : # 열의 우측 끝까지 도달 후에 이동할 블록이 남아있다면 블록 이동
            board[i][p] = x
    return board

#오른쪽방향
def right(board) :
    for i in range(N) :
        p = N - 1 # 열의 가장 우측
        x = 0
        for j in range(N-1, -1, -1) :
            if board[i][j] == 0 : # 빈칸이면 continue
                continue
            if x == 0 : # x가 비어있으면 더해줄 이전 블록이 없다는 의미이므로 x를 변경
                x = board[i][j]
            else :
                if x == board[i][j] : # 블록의 숫자가 같다면
                    board[i][p] = x * 2
                    x = 0 # 블록을 더했으므로 0으로 다시 초기화
                    p -= 1 # 열에서 갈 수 있는 가장 우측을 채웠으므로 다음 블록이 이동하기 위한 위치 감소
                else :
                    board[i][p] = x # 이동할 곳에 지난 블록 x를 저장
                    x = board[i][j] # 이전 블록을 새로운 블록으로 변경
                    p -= 1 # 열에서 갈 수 있는 가장 우측을 채웠으므로 다음 블록이 이동하기 위한 위치 감소
            board[i][j] = 0 # 블록 이동했으므로 비워줌
        if x != 0 : # 열의 좌측 끝까지 도달 후에 이동할 블록이 남아있다면 블록 이동
            board[i][p] = x
    return board

#위의 방향일 때
def up(board) :
    for i in range(N) : # 열
        p = 0 # 행의 가장 위
        x = 0
        for j in range(N) :
            if board[j][i] == 0 : # 빈칸이면 continue
                continue
            if x == 0 : # x가 비어있으면 더해줄 블록이 없다는 의미이므로 x를 변경
                x = board[j][i]
            else :
                if x == board[j][i] :
                    board[p][i] = x * 2
                    x = 0
                    p += 1
                else :
                    board[p][i] = x
                    x = board[j][i]
                    p += 1
            board[j][i] = 0
        if x != 0 :
            board[p][i] = x
    return board

#아래방향
def down(board):
    for i in range(N):
        p = N-1 #행의 가장 아래
        x = 0 #이전 값
        for j in range(N-1, -1, -1):
            if board[j][i] == 0: #빈칸이면 아무것도 없음
                continue
            if x == 0 : #x가 비어있으면 더해줄 블록
                x = board[j][i]
            else :
                if x == board[j][i] : #블록이 서로 같을 때
                    board[p][i] = x*2
                    x= 0
                    p -= 1
                else : #블록이 서로 같지 않을 때, 기존값 유지
                    board[p][i] = x
                    x = board[j][i]
                    p -=1
            board[j][i]=0
        if x!=0:
            board[p][i] = x
    return board


def solution(board, cnt):
    global result
    if cnt ==5:
        for i in range(N):
            for j in range(N):
                result = max(result, board[i][j])
        return

    solution(left(deepcopy(board)), cnt+1) # 좌측이동
    solution(right(deepcopy(board)), cnt + 1)  # 우측이동
    solution(up(deepcopy(board)), cnt + 1)  # 위쪽이동
    solution(down(deepcopy(board)), cnt + 1)  # 아래이동

solution(map, 0)
print(result)