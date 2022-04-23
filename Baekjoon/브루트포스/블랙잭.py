N,M = map(int,input().split())
card = list(map(int, input().split()))
sum = 0

for i in range(N): #삼중포문을 통해 값 구하기
    for j in range(i+1,N):
        for k in range(j+1,N):
            if card[i]+card[j]+card[k]> M:
                continue
            else:
                sum = max(sum, card[i]+card[j]+card[k])

print(sum)