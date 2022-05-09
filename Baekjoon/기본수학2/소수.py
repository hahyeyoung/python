'''
소수 판별 알고리즘
- 1을 제외하고 자연수로 나누어지지 않은 것 : 소수


'''

M = int(input())
N = int(input())

sosu = []

for i in range(M,N+1):
    if i!=1 :
        check = True
        for j in range(2,i):
            if i % j == 0 :
                check = False
                break
        if check :
            sosu.append(i)
if len(sosu) == 0:
    print(-1)
else :
    print(sum(sosu))
    print(min(sosu))

