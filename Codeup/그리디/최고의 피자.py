#입력값
N = int(input()) #토핑종류수
A,B = map(int, input().split()) #도우, 토핑 값
C = int(input()) # 도우 칼로리
toping = []
for i in range(N) : #토핑칼로리 입력
    toping.append(int(input()))
toping.sort(reverse=True) # 칼로리 높은 순으로 정렬
print(toping)

#변수
price = A
cal = C
pizzacal = 0

#계산값







