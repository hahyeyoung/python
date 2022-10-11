from collections import deque
#입력값
toni = []
for i in range(4):
    toni.append(deque(list(map(int, input().rstrip()))))
k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    r = [] #처음 톱니 상태
    for j in range(4):
        r.append([toni[j][6],toni[j][2]])
    a = a-1
    #왼쪽에 있는 톱니 돌리기
    if a!= 0:
        for i in range(a,0,-1):
            if r[i][0] != r[i-1][1]:
                if (a-(i-1))%2 == 0:
                    toni[i-1].rotate(b)
                elif (a-(i-1))%2 != 0:
                    toni[i - 1].rotate(-1*b)
            elif r[i][0] == r[i-1][1]:
                break
    if a !=3 :
        for i in range(a,3):
            if r[i][1] != r[i+1][0]:
                if (a-(i+1))%2 == 0:
                    toni[i+1].rotate(b)
                elif (a-(i+1))%2 != 0:
                    toni[i + 1].rotate(-1*b)
            elif r[i][1] == r[i+1][0]:
                break
    toni[a].rotate(b)

result = 0
if toni[0][0] == 1:
    result +=1
if toni[1][0] == 1:
    result +=2
if toni[2][0] == 1:
    result +=4
if toni[3][0] == 1:
    result +=8
print(result)