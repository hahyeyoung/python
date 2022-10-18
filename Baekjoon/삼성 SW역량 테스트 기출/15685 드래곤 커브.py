
#우상좌하
dx= [1,0,-1,0]
dy= [0,-1,0,1]

N = int(input())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))
connect = [[] for _ in range(N)] #연결된 선분 저장

for i in range(N):
    x,y,d,g = data[i]
    connect[i].append(d) #방향삽입
    for _ in range(g):
        reverse = list(reversed(connect[i])) #뒤집기,
        for j in reverse:
            if j+1 == 4 : #4일 때
                connect[i].append(0)
            else:
                connect[i].append(j+1)

area = [[0]*101 for _ in range(101)] #정사각형 지도

for i in range(N):
    x,y,d,g = data[i]
    area[y][x] =1
    for j in connect[i]:
        x,y = x+dx[j], y+dy[j]
        if 0<=x<=100 and 0<=y<=100:
            area[y][x] = 1

result=0
for i in range(100):
    for j in range(100):
        if area[i][j] and area[i][j + 1] and area[i + 1][j] and area[i + 1][j + 1]:
            result += 1

print(result)