n = int(input())
num = []

for i in range(n):
    a = list(map(int,input().split()))
    num.append(a)

num.sort(key=lambda x:(x[0],x[1]))

for i, j in num :
    print(i,j)
