N = int(input())
road = list(map(int,input().split()))
ju = list(map(int,input().split()))

result = 0
m = ju[0]

for i in range(N-1):
    if ju[i] < m :
        m = ju[i]
    result += m*road[i]
print(result)