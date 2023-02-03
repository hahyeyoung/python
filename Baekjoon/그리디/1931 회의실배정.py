N = int(input())
num = []
for i in range(N):
    a = list(map(int,input().split()))
    num.append(a)
num.sort(key=lambda x : (x[1],x[0]))

last = 0
result = 0

for i,j in num:
    if i>= last:
        result +=1
        last = j
print(result)


