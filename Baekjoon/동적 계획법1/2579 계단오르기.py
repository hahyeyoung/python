#1안
import sys
input = sys.stdin.readline
arr = []
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
for i in range(3,l):
    dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

print(dp.pop())

N = int(input())
stair = [0]*301
for i in range(N):
    stair[i]=int(input())

#2안
DP = [0]*301
DP[0] = stair[0]
DP[1] = stair[0]+stair[1]
DP[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i])

print(DP[N-1])