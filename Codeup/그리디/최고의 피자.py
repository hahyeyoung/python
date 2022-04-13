#입력값
N = int(input()) #토핑종류수
A,B = map(int, input().split()) #도우, 토핑 값
C = int(input()) # 도우 칼로리
toping = []
for i in range(N) : #토핑칼로리 입력
    toping.append(int(input()))
toping.sort(reverse=True) # 칼로리 높은 순으로 정렬

#변수
price = 0 #전체적인 가격
cal = 0 #전체칼로리
pizzacal = [] #피자칼로리

#계산값 #1) 가격(피자도우가격 + 토핑개수*가격) #2) 칼로리(피자칼로리 + 토핑칼로리)
for j in range(0,N) :
    price = A+(B*j)
    cal = C+sum(toping[:j])
    pizzacal.append(cal/price)
print(int(max(pizzacal)))







