#오늘부터 N+1되는날 퇴사를 하기 위함, 남은 N일 동안 최대한 많은 상담을 하려 함
#최대한 많은 상담, 하루에 하나씩 서로 다른 상담
# 걸리는 시간 T, 상담금액 P
# 최대이익을 얻을 수 있는 방법
N = int(input())
t = []
p = []
dp = []
for i in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(N - 1, -1, -1):
    if t[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])