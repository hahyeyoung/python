#총 N개의 시험장, i번 시험장 응시자의 수는 Ai명
#감독관 : 총감독-B, 부감독관-C
#총감독은 한명, 부감독은 여러명 가능
#감독관 수의 최솟값
N = int(input())
A = list(map(int,input().split()))
B, C = map(int, input().split())

result = N
for i in range(N): #응시자수 구하는 코드
    sub = A[i]-B
    if sub <= C and sub>0 : #총감독 1명 + 부감독 1명만 필요할 경우
        result += 1
    elif sub > C: #부감독이 여려명 일때
        if (sub)%C == 0 : # 홀수일 때
            result = result+(sub//C)
        else:
            result = result + (sub//C)+1
print(result)