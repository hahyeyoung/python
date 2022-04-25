N= int(input())
sum = []

for i in range(N):
    a,b = map(int, input().split())
    sum.append(a+b)

for i in range(N):
    print(f'Case #{i+1}: {sum[i]}')