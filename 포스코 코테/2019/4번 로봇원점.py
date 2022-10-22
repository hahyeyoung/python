#U,D,R,L 방향을 볼때, 로봇이 다시 원점으로 돌아올 수 있는 경우의 수
from itertools import combinations
derection = list(input())

result = 0
for i in range(2,len(derecion),2):
    combi = list(combinations(derection),i)

