'''
두 원의 위치관계, 원의 방정식
 - 두 개의 터렛 각각에서 상태편 마린까지의 거리가 주어졌을 때, 타깃이 위치할 수 있는
경우의 수를 출력하는 문제
- 두 원의 위치 관계 활용

- 원이 겹쳐질 때, 원이 두개가 포개질때,
'''

import math

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 +(y1-y2)**2) #두 원의 거리
    if distance == 0 and r1 == r2 : # 두원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance : # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) : # 두원이 서로다른 두 점에서 만날 때
        print(2)
    else :
        print(0)
