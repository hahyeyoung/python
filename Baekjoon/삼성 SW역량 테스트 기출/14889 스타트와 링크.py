#스타트링크에 다니는 사람들이 모여서  축구를 하려 한다
# 축구를 위한 사람이 총 N명, N은 짝수, N/2 스타트 팀과 링크 팀
# 번호 1~N 능력치, S는, i번 사람과 j번 사람이 같은 팀에 속했을 때 팀시너지
# 모든 쌍의 능력치 S의 합
# 두 팀의 차이값이 최소가 되게 하려 함
import sys

input = sys.stdin.readline

N = int(input())
S = []
result = 1e9 #결과값 출력을 위한 result값을 문제의 범위를 벗어나는 큰 수로 초기화
visited = [False] * (N + 1) #방문여부를 확인하는 리스트
for _ in range(N):
    S.append(list(map(int, input().split())))

#팀별 나누기
def dfs(depth, idx):
    global result
    if depth == (N // 2): # N // 2 번만큼 재귀를 돌면
        start_team, link_team = 0, 0 #start팀과 link팀 0으로 선언
        for i in range(N):
            for j in range(i + 1, N): #이중 리스트의 열은 굳이 0부터 돌필요가 없기 때문에 i + 1 로 범위를 좁혀준다.
                if visited[i] and visited[j]: #만약 i,j 둘다 방문 했다면
                    start_team += (S[i][j] + S[j][i]) #방문한 사람을 스타트팀에 더해준다.
                elif not visited[i] and not visited[j]: # 방문 안한 i j 는 링크팀이므로
                    link_team += (S[i][j] + S[j][i])  #방문안한 사람을 링크팀에 더해준다
        result = min(result, abs(start_team-link_team))
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False
dfs(0,0)
print(result)
