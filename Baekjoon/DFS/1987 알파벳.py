# 세로 R, 가로 C 대문자 알파벳이 하나씩 적혀 있음
#좌측 상단 칸(1행 1열) 말이 있음
# 상하좌우 한칸이동, 새로 이동한 칸 지금까지 알파벳과 달라야 함
#말이 몇칸 지날 수 있는지(좌측 상단 칸도 포함)
import sys
sys.setrecursionlimit(4000)
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(input().strip()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
word = set()
def dfs(x,y, count):
    global cnt
    cnt = max(cnt,count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and not graph[nx][ny] in word:
            word.add(graph[nx][ny])
            dfs(nx,ny,count+1)
            word.remove(graph[nx][ny])
word.add(graph[0][0])
dfs(0,0,1)
print(cnt)
