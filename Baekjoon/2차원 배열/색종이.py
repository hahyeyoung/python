paper = [[0,0,0,0,0,0,0,0,0,0]*10 for _ in range(101)]

k = int(input())

for i in range(k):
    a, b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            paper[j][k] = 1
result = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            result +=1
print(result)