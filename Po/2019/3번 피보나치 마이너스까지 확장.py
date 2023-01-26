#백준 1788 피보나치 수의 확장
n = int(input())
flag = 0
if n>0:
    flag = 1
elif n<0:
    flag = -1
dp = [0,1]
for _ in range(2,abs(n)+1):
    dp.append((dp[-1]+dp[-2]))
print(dp[abs(n)])
