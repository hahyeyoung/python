N = int(input())
num = [0]+list(map(int,input().split()))
result = [-1001]*(N+1)

for i in range(1,N+1):
    result[i] = max(num[i], result[i-1]+num[i])
print(max(result))

