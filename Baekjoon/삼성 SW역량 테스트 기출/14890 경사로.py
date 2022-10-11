N, L = map(int, input().split())
road = []
for i in range(N):
    road.append(list(map(int, input().split())))

#길 지나가기 및 경사로 설치
'''
경사로는 낮은 칸에 놓이며, 낮은칸과 높은 칸의 차이는 1이어야 함
L이 연속되어야 함
'''
def check_road(N,L,road):
    ramp = [0]*N
    for i in range(N-1):
        if road[i] != road[i+1]:
            if abs(road[i]-road[i+1])>1:
                return False
            else :
                if road[i]-road[i+1] == 1:
                    if i+1+L > N :
                        return False
                    check = road[i+1]
                    for j in range(i+1,i+1+L):
                        if ramp[j] or road[j] != check : return False
                        ramp[j] =1
                elif road[i] - road[i+1] == -1:
                    if i-L < -1 : return False
                    check = road[i]
                    for j in range(i ,i-L, -1):
                        if ramp[j] or road[j] != check : return False
                        ramp[j] = 1
    return True

cnt = 0
for i in road :
    if check_road(N,L,i) : cnt+=1
for j in range(N):
    if check_road(N,L,[road[i][j] for i in range(N)]) : cnt +=1

print(cnt)